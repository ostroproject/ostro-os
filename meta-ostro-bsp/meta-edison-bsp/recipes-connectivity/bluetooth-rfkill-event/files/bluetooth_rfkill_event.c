/******************************************************************************
 *
 * Copyright (c) 2014, Intel Corporation.

 * This program is free software; you can redistribute it and/or modify it
 * under the terms of version 2 of the GNU General Public License as
 * published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
 * more details.
 *
 * You should have received a copy of the GNU General Public License along with
 * this program; if not, write to the Free Software Foundation, Inc., 59
 * Temple Place - Suite 330, Boston, MA  02111-1307, USA.
 *
 *******************************************************************************/

/*******************************************************************************
 **
 ** Name:           bluetooth_rfkill_event.c
 **
 ** Description:    This program is listening rfkill event and detect when a
 **                 'power' rfkill interface is unblocked and trigger FW patch
 **                 download for detected chip.
 **
 *******************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <fcntl.h>
#include <string.h>
#include <sys/poll.h>
#include <sys/time.h>
#include <sys/ioctl.h>
#include <limits.h>
#include <glib.h>
#include <bluetooth/bluetooth.h>
#include <bluetooth/hci.h>
#include <bluetooth/hci_lib.h>


enum {
    BT_PWR,
    BT_HCI,
};

/* list of all supported chips:
   name is defined in the kernel driver implementing rfkill interface for power */
#define BCM_RFKILL_NAME "bcm43xx Bluetooth\n"
#define BCM_43341_UART_DEV "/dev/ttyMFD0"
#define BD_ADD_FACTORY_FILE "/factory/bluetooth_address"
char factory_bd_add[18];
const char default_bd_addr[] = "00:43:34:b1:be:ef";

/* attempt to set hci dev UP */
#define MAX_RETRY 10

enum rfkill_operation {
    RFKILL_OP_ADD = 0,
    RFKILL_OP_DEL,
    RFKILL_OP_CHANGE,
    RFKILL_OP_CHANGE_ALL,
};

enum rfkill_type {
    RFKILL_TYPE_ALL = 0,
    RFKILL_TYPE_WLAN,
    RFKILL_TYPE_BLUETOOTH,
    RFKILL_TYPE_UWB,
    RFKILL_TYPE_WIMAX,
    RFKILL_TYPE_WWAN,
    RFKILL_TYPE_GPS,
    RFKILL_TYPE_FM,
    NUM_RFKILL_TYPES,
};

struct rfkill_event {
    unsigned int  idx;
    unsigned char type;
    unsigned char op;
    unsigned char soft, hard;
} __packed;

/* HCI UART driver initialization utility; usually it takes care of FW patch download as well */
char hciattach[PATH_MAX];
char hciattach_options[PATH_MAX];
char hci_uart_default_dev[PATH_MAX] = BCM_43341_UART_DEV;

gboolean hci_dev_registered;
int bt_pwr_rfkill_idx;

struct main_opts {
    /* 'fork' will keep running in background the hciattach utility; N/A if enable_hci is FALSE */
    gboolean    enable_fork;
    /* send enable Low Power Mode to Broadcom bluetooth controller; needed if power driver implements it */
    gboolean    enable_lpm;
    /* register the hci device */
    gboolean    enable_hci;
    /* set UART baud rate */
    gboolean    set_baud_rate;
    int         baud_rate;
    /* download FW patch */
    gboolean    dl_patch;
    char*       fw_patch;
    /* UART device used for bluetooth; platform dependant */
    char*       uart_dev;
    /* configure BD address */
    gboolean    set_bd;
    char*       bd_add;
    /* set SCO routing for audio interface */
    gboolean    set_scopcm;
    char*       scopcm;
};

struct main_opts main_opts;

static const char * const supported_options[] = {
    "fork",
    "lpm",
    "reg_hci",
    "baud_rate",
    "fw_patch",
    "uart_dev",
    "scopcm",
};

void init_config()
{
    memset(&main_opts, 0, sizeof(main_opts));

    main_opts.enable_fork = TRUE;
    main_opts.enable_lpm = TRUE;
    main_opts.enable_hci = FALSE;
    main_opts.set_baud_rate = FALSE;
    main_opts.dl_patch = FALSE;
    main_opts.set_bd = FALSE;
    main_opts.set_scopcm = FALSE;
}

GKeyFile *load_config(const char *file)
{
    GError *err = NULL;
    GKeyFile *keyfile;

    keyfile = g_key_file_new();

    g_key_file_set_list_separator(keyfile, ',');

    if (!g_key_file_load_from_file(keyfile, file, 0, &err)) {
        if (!g_error_matches(err, G_FILE_ERROR, G_FILE_ERROR_NOENT))
            error("Parsing %s failed: %s", file, err->message);
        g_error_free(err);
        g_key_file_free(keyfile);
        return NULL;
    }

    return keyfile;
}

void check_config(GKeyFile *config)
{
    char **keys;
    int i;

    if (!config)
        return;

    keys = g_key_file_get_groups(config, NULL);

    for (i = 0; keys != NULL && keys[i] != NULL; i++) {
        if (!g_str_equal(keys[i], "General"))
            warn("Unknown group %s in main.conf", keys[i]);
    }

    g_strfreev(keys);

    keys = g_key_file_get_keys(config, "General", NULL, NULL);

    for (i = 0; keys != NULL && keys[i] != NULL; i++) {
        gboolean found;
        unsigned int j;

        found = FALSE;
        for (j = 0; j < G_N_ELEMENTS(supported_options); j++) {
            if (g_str_equal(keys[i], supported_options[j])) {
                found = TRUE;
                break;
            }
        }

        if (!found)
            warn("Unknown key %s in main.conf", keys[i]);
    }

    g_strfreev(keys);
}

void parse_config(GKeyFile *config)
{
    GError *err = NULL;
    char *str;
    int val;
    gboolean boolean;

    if (!config)
        return;

    check_config(config);

    boolean = g_key_file_get_boolean(config, "General", "fork", &err);
    if (err) {
        g_clear_error(&err);
    } else
        main_opts.enable_fork = boolean;

    boolean = g_key_file_get_boolean(config, "General", "lpm", &err);
    if (err) {
        g_clear_error(&err);
    } else
        main_opts.enable_lpm = boolean;

    boolean = g_key_file_get_boolean(config, "General", "reg_hci", &err);
    if (err) {
        g_clear_error(&err);
    } else
        main_opts.enable_hci = boolean;

    val = g_key_file_get_integer(config, "General", "baud_rate", &err);
    if (err) {
        g_clear_error(&err);
    } else {
        main_opts.baud_rate = val;
        main_opts.set_baud_rate = TRUE;
    }

    str = g_key_file_get_string(config, "General", "fw_patch", &err);
    if (err) {
        g_clear_error(&err);
    } else {
        g_free(main_opts.fw_patch);
        main_opts.fw_patch = str;
        main_opts.dl_patch = TRUE;
    }

    str = g_key_file_get_string(config, "General", "uart_dev", &err);
    if (err) {
        g_clear_error(&err);
        main_opts.uart_dev = hci_uart_default_dev;
    } else {
        g_free(main_opts.uart_dev);
        main_opts.uart_dev = str;
    }

    str = g_key_file_get_string(config, "General", "scopcm", &err);
    if (err) {
        g_clear_error(&err);
    } else {
        g_free(main_opts.scopcm);
        main_opts.scopcm = str;
        main_opts.set_scopcm = TRUE;
    }
}

gboolean check_bd_format(const char* bd_add)
{
    int i, len;

    len = strlen(bd_add);

    if (len != 17)
        return FALSE;

    for (i = 0 ; i < len; i++)
    {
        /* check that format is xx:xx: ... etc. */
        if ((isxdigit(bd_add[i]) && i%3 != 2) ||
            (bd_add[i] == ':' && i%3 == 2))
        {
            ;
        }
        else
        {
            return FALSE;
        }
    }

    return TRUE;
}

void load_bd_add(void)
{
    FILE *fp;
    int ret;

    fp = fopen(BD_ADD_FACTORY_FILE, "r");

    /* if BD add file has not been provisioned do not send VSC to set BD address: the one configured in OTP will be used or default FW one */
    if (fp == NULL)
    {
        main_opts.set_bd = FALSE;
        return;
    }

    ret = fscanf(fp, "%17c", factory_bd_add);

    /* if factory BD address is not well formatted or not present do not send VSC to set BD address: the one configured in OTP will be used or default FW one */
    if (!(ret == 1 && check_bd_format(factory_bd_add)))
    {
        main_opts.set_bd = FALSE;
    }
    else
    {
        main_opts.bd_add = factory_bd_add;
        main_opts.set_bd = TRUE;
    }

    fclose(fp);

}

void read_config(char* file)
{
    GKeyFile *config;
    char *cur = hciattach_options;
    const char *end = hciattach_options + sizeof(hciattach_options);

    /* set first default values and then load configured ones */
    init_config();
    config = load_config(file);
    parse_config(config);
    load_bd_add();

    /* set always configured options: use same configured baud-rate also for download, and ignore first 2 bytes (needed by bcm43341 and more recent brcm bt chip) */
    cur += snprintf(cur, end-cur, "%s", "--use_baudrate_for_download --no2bytes");

    /* concatenate configured options */
    if ((cur < end) && (main_opts.enable_fork)) {
        cur += snprintf(cur, end-cur," %s", "--enable_fork");
    }
    if ((cur < end) && (main_opts.enable_lpm)) {
        cur += snprintf(cur, end-cur," %s", "--enable_lpm");
    }
    if ((cur < end) && (main_opts.enable_hci)) {
        cur += snprintf(cur, end-cur," %s", "--enable_hci");
    }
    if ((cur < end) && (main_opts.set_baud_rate)) {
        cur += snprintf(cur, end-cur," --baudrate %d", main_opts.baud_rate);
    }
    if ((cur < end) && (main_opts.dl_patch)) {
        cur += snprintf(cur, end-cur," --patchram %s", main_opts.fw_patch);
    }
    if ((cur < end) && (main_opts.set_bd)) {
        cur += snprintf(cur, end-cur," --bd_addr %s", main_opts.bd_add);
    }
    if ((cur < end) && (main_opts.set_scopcm)) {
        cur += snprintf(cur, end-cur," --scopcm %s", main_opts.scopcm);
    }
}

void free_hci()
{
    char cmd[PATH_MAX];

    snprintf(cmd, sizeof(cmd), "pidof %s", hciattach);

    if (!system(cmd))
    {
        snprintf(cmd, sizeof(cmd), "killall %s", hciattach);
        system(cmd);
        printf("killing %s\n", hciattach);
        fflush(stdout);
    }
}

void attach_hci()
{
    char hci_execute[PATH_MAX];

    snprintf(hci_execute, sizeof(hci_execute), "%s %s %s", hciattach, hciattach_options, main_opts.uart_dev);

    printf("execute %s\n", hci_execute);
    fflush(stdout);

    system(hci_execute);

    /* remember if hci device has been registered (in case conf file is changed) */
    hci_dev_registered = main_opts.enable_hci;
}

void up_hci(int hci_idx)
{
    int sk, i;
    struct hci_dev_info hci_info;

    sk = socket(AF_BLUETOOTH, SOCK_RAW, BTPROTO_HCI);

    if (sk < 0)
    {
        perror("Fail to create bluetooth hci socket");
        return;
    }

    memset(&hci_info, 0, sizeof(hci_info));

    hci_info.dev_id = hci_idx;

    for (i = 0;  i < MAX_RETRY; i++)
    {
        if (ioctl(sk, HCIGETDEVINFO, (void *) &hci_info) < 0)
        {
            perror("Failed to get HCI device information");
            /* sleep 100ms */
            usleep(100*1000);
            continue;
        }

        if (hci_test_bit(HCI_RUNNING, &hci_info.flags) && !hci_test_bit(HCI_INIT, &hci_info.flags))
        {
            /* check if kernel has already set device UP... */
            if (!hci_test_bit(HCI_UP, &hci_info.flags))
            {
                if (ioctl(sk, HCIDEVUP, hci_idx) < 0)
                {
                    /* ignore if device is already UP and ready */
                    if (errno == EALREADY)
                        break;

                    perror("Fail to set hci device UP");
                }
            }
            break;
        }

        /* sleep 100ms */
        usleep(100*1000);
    }

    close(sk);
}

/* calling this routine to be sure to have rfkill hci bluetooth interface unblocked:
   if user does:
   - 'rfkill block bluetooth' and then
   - 'rfkill unblock 2'
   once hci bluetooth is registered back it will be blocked */
void rfkill_bluetooth_unblock()
{
    int fd, sk, times;
    int ret = -1;
    struct rfkill_event event;

    fd = open("/dev/rfkill", O_RDWR | O_CLOEXEC);
    if (fd < 0)
    {
        perror("fail to open rfkill interface");
        return;
    }
    memset(&event, 0, sizeof(event));
    event.op = RFKILL_OP_CHANGE_ALL;
    event.type = RFKILL_TYPE_BLUETOOTH;
    event.soft = 0;
    if (write(fd, &event, sizeof(event)) < 0)
    {
        perror("fail to unblock rfkill bluetooth");
    }
    close(fd);

}

int main(int argc, char **argv)
{
    struct rfkill_event event;
    struct timeval tv;
    struct pollfd p;
    ssize_t len;
    int fd, fd_name, n, type;
    int ret, hci_dev_id;
    char *script;
    char sysname[PATH_MAX];

    /* this code is ispired by rfkill source code */

    fd = open("/dev/rfkill", O_RDONLY);
    if (fd < 0) {
        perror("Can't open RFKILL control device");
        return fd;
    }

    memset(&p, 0, sizeof(p));
    p.fd = fd;
    p.events = POLLIN | POLLHUP;

    while (1) {
        n = poll(&p, 1, -1);
        if (n < 0) {
            perror("Failed to poll RFKILL control device");
            break;
        }

        if (n == 0)
            continue;

        len = read(fd, &event, sizeof(event));
        if (len < 0) {
            perror("Reading of RFKILL events failed");
            break;
        }

        if (len != sizeof(event)) {
            perror("Wrong size of RFKILL event");
            break;
        }

        /* ignore event for others interfaces (not bluetooth) */
        if (event.type != RFKILL_TYPE_BLUETOOTH)
            continue;

        gettimeofday(&tv, NULL);
        printf("%ld.%06u: idx %u type %u op %u soft %u hard %u\n",
              (long) tv.tv_sec, (unsigned int) tv.tv_usec,
              event.idx, event.type, event.op, event.soft, event.hard);
        fflush(stdout);

        /* try to read rfkill interface name only if event is not a remove one, in this case call free_hci */
        if (event.op != RFKILL_OP_DEL)
        {
            /* get the name to check the bt chip */
            snprintf(sysname, sizeof(sysname), "/sys/class/rfkill/rfkill%u/name", event.idx);

            fd_name = open(sysname, O_RDONLY);
            if (fd_name < 0)
            {
                perror("fail to open rfkill name");
                continue;
            }

            memset(sysname, 0, sizeof(sysname));

            /* read name */
            if (read(fd_name, sysname, sizeof(sysname) - 1) < 0)
            {
                perror("fail to read rfkill name");
                close(fd_name);
                continue;
            }

            close(fd_name);

            /* based on chip read its config file, if any, and define the hciattach utility used to dowload the patch */
            if (strncmp(BCM_RFKILL_NAME,sysname, sizeof(BCM_RFKILL_NAME)) == 0)
            {
                read_config("/etc/firmware/bcm43341.conf");
                snprintf(hciattach, sizeof(hciattach), "brcm_patchram_plus");
                type = BT_PWR;
            }
            else if (g_str_has_prefix(sysname, "hci") )
            {
                type = BT_HCI;
                hci_dev_id = atoi(sysname + 3);
            }
            else
                continue;
        }

        switch (event.op) {
        case RFKILL_OP_CHANGE:
        case RFKILL_OP_CHANGE_ALL:
        case RFKILL_OP_ADD:
            if (event.soft == 0 && event.hard == 0)
            {
                if (type == BT_PWR)
                {
                    /* if unblock is for power interface: download patch and eventually register hci device */
                    free_hci();
                    attach_hci();
                    /* force to unblock also the bluetooth hci rfkill interface if hci device was registered */
                    if (hci_dev_registered)
                        rfkill_bluetooth_unblock();
                }
                else if (type == BT_HCI && hci_dev_registered)
                {
                    /* wait unblock on hci bluetooth interface and force device UP */
                    up_hci(hci_dev_id);
                }
            }
            else if (type == BT_PWR && hci_dev_registered)
            {
                /* for a block event on power interface force unblock of hci device interface */
                free_hci();
            }

            /* save index of rfkill interface for bluetooth power */
            if (event.op == RFKILL_OP_ADD && type == BT_PWR)
                bt_pwr_rfkill_idx = event.idx;
        break;
        case RFKILL_OP_DEL:
            /* in case pwr rfkill interface is removed, unregister hci dev if it was registered */
            if (bt_pwr_rfkill_idx == event.idx && hci_dev_registered)
                free_hci();
        break;
        default:
            continue;
        }

    }

    close(fd);

    return 0;
}
