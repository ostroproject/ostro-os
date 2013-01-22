User Space Graphics Driver Binary License

Copyright (c) 2008, Intel Corporation. 
Portions (c), Imagination Technology, Ltd. 
All rights reserved. 
Redistribution and Use. Redistribution and use in binary form, without modification, of the software code provided with this license (“Software”), are permitted provided that the following conditions are met: 
• Redistributions must reproduce the above copyright notice and this license in the documentation and/or other materials provided with the Software. 
• Neither the name of Intel Corporation nor the name of Imagination Technology, Ltd may be used to endorse or promote products derived from the Software without specific prior written permission. 
• The Software can only be used in connection with the Intel hardware designed to use the Software as outlined in the documentation. No other use is authorized. 
• No reverse engineering, decompilation, or disassembly of the Software is permitted. 
• The Software may not be distributed under terms different than this license. 

Limited Patent License. Intel Corporation grants a world-wide, royalty-free, non-exclusive license under patents it now or hereafter owns or controls to make, have made, use, import, offer to sell and sell (“Utilize”) the Software, but solely to the extent that any such patent is necessary to Utilize the Software alone. The patent license shall not apply to any combinations which include the Software. No hardware per se is licensed hereunder. 
Ownership of Software and Copyrights. Title to all copies of the Software remains with the copyright holders. The Software is copyrighted and protected by the laws of the United States and other countries, and international treaty provisions. 
DISCLAIMER. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNERS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. 
/*
* (C) Copyright IBM Corporation 2002, 2004 
* All Rights Reserved. 
* 
* Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
* documentation files (the "Software"), to deal in the Software without restriction, including without limitation on 
* the rights to use, copy, modify, merge, publish, distribute, sub license, and/or sell copies of the Software, and to 
* permit persons to whom the Software is furnished to do so, subject to the following conditions: 
*
* The above copyright notice and this permission notice (including the next 
* paragraph) shall be included in all copies or substantial portions of the 
* Software. 
*
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
* FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL 
* VA LINUX SYSTEM, IBM AND/OR THEIR SUPPLIERS BE LIABLE FOR ANY CLAIM, 
* DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
* OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE 
* USE OR OTHER DEALINGS IN THE SOFTWARE. 
*/
 
* Mesa 3-D graphics library 
* Version: 7.1 
* 
* Copyright (C) 1999-2007 Brian Paul All Rights Reserved. 
* 
* Permission is hereby granted, free of charge, to any person obtaining a 
* copy of this software and associated documentation files (the "Software"), 
* to deal in the Software without restriction, including without limitation 
* the rights to use, copy, modify, merge, publish, distribute, sublicense, 
* and/or sell copies of the Software, and to permit persons to whom the 
* Software is furnished to do so, subject to the following conditions: 
* 
* The above copyright notice and this permission notice shall be included 
* in all copies or substantial portions of the Software. 
* 
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS 
* OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
* BRIAN PAUL BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN 
* AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN 
* CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 
*/ 
/************************************************************************** 
* 
* Copyright (c) Intel Corp. 2007. 
* All Rights Reserved. 
* 
* Intel funded Tungsten Graphics (http://www.tungstengraphics.com) to 
* develop this driver. 
* 
* Permission is hereby granted, free of charge, to any person obtaining a 
* copy of this software and associated documentation files (the 
* "Software"), to deal in the Software without restriction, including 
* without limitation the rights to use, copy, modify, merge, publish, 
* distribute, sub license, and/or sell copies of the Software, and to 
* permit persons to whom the Software is furnished to do so, subject to 
* the following conditions: 
* 
* The above copyright notice and this permission notice (including the 
* next paragraph) shall be included in all copies or substantial portions 
* of the Software. 
* 
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
* FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL 
* THE COPYRIGHT HOLDERS, AUTHORS AND/OR ITS SUPPLIERS BE LIABLE FOR ANY CLAIM, 
* DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
* OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE 
* USE OR OTHER DEALINGS IN THE SOFTWARE. 
* 
**************************************************************************/ 

* Copyright (c) 2006-2007 Intel Corporation 
* 
* Permission is hereby granted, free of charge, to any person obtaining a 
* copy of this software and associated documentation files (the "Software"), 
* to deal in the Software without restriction, including without limitation 
* the rights to use, copy, modify, merge, publish, distribute, sublicense, 
* and/or sell copies of the Software, and to permit persons to whom the 
* Software is furnished to do so, subject to the following conditions: 
* 
* The above copyright notice and this permission notice (including the next 
* paragraph) shall be included in all copies or substantial portions of the 
* Software. 
* 
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
* THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
* OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
* SOFTWARE. 
* 
* Authors: 
* Eric Anholt <eric@anholt.net> 
* Thomas Hellstrom <thomas-at-tungstengraphics-dot-com> 
* 
*/ 
/************************************************************************** 
Copyright 1998-1999 Precision Insight, Inc., Cedar Park, Texas. 
Copyright © 2002 David Dawes 
All Rights Reserved. 
Permission is hereby granted, free of charge, to any person obtaining a 
copy of this software and associated documentation files (the 
"Software"), to deal in the Software without restriction, including 
without limitation the rights to use, copy, modify, merge, publish, 
distribute, sub license, and/or sell copies of the Software, and to 
permit persons to whom the Software is furnished to do so, subject to 
the following conditions: 
The above copyright notice and this permission notice (including the 
next paragraph) shall be included in all copies or substantial portions 
of the Software. 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS 
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. 
IN NO EVENT SHALL PRECISION INSIGHT AND/OR ITS SUPPLIERS BE LIABLE FOR 
ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 

**************************************************************************/ 
/* 
* Authors: 
* Keith Whitwell <keith@tungstengraphics.com> 
* David Dawes <dawes@xfree86.org> 
* 
* Updated for Dual Head capabilities: 
* Alan Hourihane <alanh@tungstengraphics.com> 
* 
* Add ARGB HW cursor support: 
* Alan Hourihane <alanh@tungstengraphics.com> 
* 
* Poulsbo port 
* Thomas Hellstrom <thomas-at-tungstengraphics-dot-com> 
*/ 
/* 
* XFree86 Xv DDX written by Mark Vojkovich (markv@valinux.com) 
*/ 
/* 
* Copyright (c) 1998-2003 by The XFree86 Project, Inc. 
* 
* Permission is hereby granted, free of charge, to any person obtaining a 
* copy of this software and associated documentation files (the "Software"), 
* to deal in the Software without restriction, including without limitation 
* the rights to use, copy, modify, merge, publish, distribute, sublicense, 
* and/or sell copies of the Software, and to permit persons to whom the 
* Software is furnished to do so, subject to the following conditions: 
* 
* The above copyright notice and this permission notice shall be included in 
* all copies or substantial portions of the Software. 
* 
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
* THE COPYRIGHT HOLDER(S) OR AUTHOR(S) BE LIABLE FOR ANY CLAIM, DAMAGES OR 
* OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
* ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR 
* OTHER DEALINGS IN THE SOFTWARE. 
* 
* Except as contained in this notice, the name of the copyright holder(s) 
* and author(s) shall not be used in advertising or otherwise to promote 
* the sale, use or other dealings in this Software without prior written 
* authorization from the copyright holder(s) and author(s). 
*/ 
/* 
** Copyright (c) 2007-2009 The Khronos Group Inc. 
** 
** Permission is hereby granted, free of charge, to any person obtaining a 
** copy of this software and/or associated documentation files (the 
** "Materials"), to deal in the Materials without restriction, including 
** without limitation the rights to use, copy, modify, merge, publish, 
** distribute, sublicense, and/or sell copies of the Materials, and to 
** permit persons to whom the Materials are furnished to do so, subject to 
** the following conditions:  

** The above copyright notice and this permission notice shall be included 
** in all copies or substantial portions of the Materials. 
** 
** THE MATERIALS ARE PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
** EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
** MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
** IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
** CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
** TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
** MATERIALS OR THE USE OR OTHER DEALINGS IN THE MATERIALS. 
*/ 
/* 
** License Applicability. Except to the extent portions of this file are 
** made subject to an alternative license as permitted in the SGI Free 
** Software License B, Version 1.0 (the "License"), the contents of this 
** file are subject only to the provisions of the License. You may not use 
** this file except in compliance with the License. You may obtain a copy 
** of the License at Silicon Graphics, Inc., attn: Legal Services, 1600 
** Amphitheatre Parkway, Mountain View, CA 94043-1351, or at: 
** 
** http://oss.sgi.com/projects/FreeB 
** 
** Note that, as provided in the License, the Software is distributed on an 
** "AS IS" basis, with ALL EXPRESS AND IMPLIED WARRANTIES AND CONDITIONS 
** DISCLAIMED, INCLUDING, WITHOUT LIMITATION, ANY IMPLIED WARRANTIES AND 
** CONDITIONS OF MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A 
** PARTICULAR PURPOSE, AND NON-INFRINGEMENT. 
** 
** Original Code. The Original Code is: OpenGL Sample Implementation, 
** Version 1.2.1, released January 26, 2000, developed by Silicon Graphics, 
** Inc. The Original Code is Copyright (c) 1991-2000 Silicon Graphics, Inc. 
** Copyright in any portions created by third parties is as indicated 
** elsewhere herein. All Rights Reserved. 
** 
** Additional Notice Provisions: The application programming interfaces 
** established by SGI in conjunction with the Original Code are The 
** OpenGL(R) Graphics System: A Specification (Version 1.2.1), released 
** April 1, 1999; The OpenGL(R) Graphics System Utility Library (Version 
** 1.3), released November 4, 1998; and OpenGL(R) Graphics with the X 
** Window System(R) (Version 1.3), released October 19, 1998. This software 
** was created using the OpenGL(R) version 1.2.1 Sample Implementation 
** published by SGI, but has not been independently verified as being 
** compliant with the OpenGL(R) version 1.2.1 Specification. 
*/ 
/* 
* This document is licensed under the SGI Free Software B License Version 
* 2.0. For details, see http://oss.sgi.com/projects/FreeB/ . 
*/ 
/* 
** License Applicability. Except to the extent portions of this file are 
** made subject to an alternative license as permitted in the SGI Free 
** Software License B, Version 1.0 (the "License"), the contents of this 
** file are subject only to the provisions of the License. You may not use 
** this file except in compliance with the License. You may obtain a copy 
** of the License at Silicon Graphics, Inc., attn: Legal Services, 1600 
** Amphitheatre Parkway, Mountain View, CA 94043-1351, or at: 
** 
** http://oss.sgi.com/projects/FreeB 
** 
** Note that, as provided in the License, the Software is distributed on an 
** "AS IS" basis, with ALL EXPRESS AND IMPLIED WARRANTIES AND CONDITIONS 
** DISCLAIMED, INCLUDING, WITHOUT LIMITATION, ANY IMPLIED WARRANTIES AND 
** CONDITIONS OF MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A 
** PARTICULAR PURPOSE, AND NON-INFRINGEMENT. 
** 
** Original Code. The Original Code is: OpenGL Sample Implementation, 
** Version 1.2.1, released January 26, 2000, developed by Silicon Graphics, 
** Inc. The Original Code is Copyright (c) 1991-2000 Silicon Graphics, Inc. 
** Copyright in any portions created by third parties is as indicated 
** elsewhere herein. All Rights Reserved. 
** 
** Additional Notice Provisions: The application programming interfaces 
** established by SGI in conjunction with the Original Code are The 
** OpenGL(R) Graphics System: A Specification (Version 1.2.1), released 
** April 1, 1999; The OpenGL(R) Graphics System Utility Library (Version 
** 1.3), released November 4, 1998; and OpenGL(R) Graphics with the X 
** Window System(R) (Version 1.3), released October 19, 1998. This software 
** was created using the OpenGL(R) version 1.2.1 Sample Implementation 
** published by SGI, but has not been independently verified as being 
** compliant with the OpenGL(R) version 1.2.1 Specification. 
*/ 
/* 
* This file contains code derived from files originally published under the 
* "SGI Free Software License B, Version 1.1", see below: 
*/ 
/* 
** License Applicability. Except to the extent portions of this file are 
** made subject to an alternative license as permitted in the SGI Free 
** Software License B, Version 1.1 (the "License"), the contents of this 
** file are subject only to the provisions of the License. You may not use 
** this file except in compliance with the License. You may obtain a copy 
** of the License at Silicon Graphics, Inc., attn: Legal Services, 1600 
** Amphitheatre Parkway, Mountain View, CA 94043-1351, or at: 
** 
** http://oss.sgi.com/projects/FreeB 
** 
** Note that, as provided in the License, the Software is distributed on an 
** "AS IS" basis, with ALL EXPRESS AND IMPLIED WARRANTIES AND CONDITIONS 
** DISCLAIMED, INCLUDING, WITHOUT LIMITATION, ANY IMPLIED WARRANTIES AND 
** CONDITIONS OF MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A 
** PARTICULAR PURPOSE, AND NON-INFRINGEMENT. 
** 
** Original Code. The Original Code is: OpenGL Sample Implementation, 
** Version 1.2.1, released January 26, 2000, developed by Silicon Graphics, 
** Inc. The Original Code is Copyright (c) 1991-2000 Silicon Graphics, Inc. 
** Copyright in any portions created by third parties is as indicated 
** elsewhere herein. All Rights Reserved.

 /*!**************************************************************************** 
@File convexitytest.c 
@Title Convex Polygon Classification 
@Author PowerVR 
@Date 23 April 2007 
@Copyright Copyright 2007 by Imagination Technologies Limited. 
@Platform ANSI 
@Description Functions for determining whether a polygon is convex or not. 
@DoxygenVer 1.0 1st Release 
******************************************************************************/ 
/* convexitytest.c */ 
/* 
* C code from the article 
* "Testing the Convexity of a Polygon" 
* by Peter Schorn and Frederick Fisher, 
* (schorn@inf.ethz.ch, fred@kpc.com) 
* in "Graphics Gems IV", Academic Press, 1994 
*/ 
/*!**************************************************************************** 
@File drvvg.h 
@Title OpenVG Driver Header 
@Author PowerVR 
@Date 22 June 2007 
@Copyright Copyright 2007- by Imagination Technologies Limited. 
@Platform ANSI 
@Description Driver version of OpenVG Macro and API definitions 
@DoxygenVer 1.0 1st Release 
******************************************************************************/ 
/********************************************************************** 
* * 
* Sample implementation of openvg.h, version 1.0.1 * 
* * 
* Copyright (c) 2005-2007 The Khronos Group * 
* * 
**********************************************************************/ 
/* 
** Copyright (c) 2007-2009 The Khronos Group Inc. 
** 
** Permission is hereby granted, free of charge, to any person obtaining a 
** copy of this software and/or associated documentation files (the 
** "Materials"), to deal in the Materials without restriction, including 
** without limitation the rights to use, copy, modify, merge, publish, 
** distribute, sublicense, and/or sell copies of the Materials, and to 
** permit persons to whom the Materials are furnished to do so, subject to 
** the following conditions: 
** 
** The above copyright notice and this permission notice shall be included 
** in all copies or substantial portions of the Materials. 
** 
** THE MATERIALS ARE PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
** EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
** MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
** IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
** CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
** TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
** MATERIALS OR THE USE OR OTHER DEALINGS IN THE MATERIALS. 
*/ 

/* 
** Copyright (c) 2007-2009 The Khronos Group Inc. 
** 
** Permission is hereby granted, free of charge, to any person obtaining a 
** copy of this software and/or associated documentation files (the 
** "Materials"), to deal in the Materials without restriction, including 
** without limitation the rights to use, copy, modify, merge, publish, 
** distribute, sublicense, and/or sell copies of the Materials, and to 
** permit persons to whom the Materials are furnished to do so, subject to 
** the following conditions: 
** 
** The above copyright notice and this permission notice shall be included 
** in all copies or substantial portions of the Materials. 
** 
** THE MATERIALS ARE PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
** EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
** MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
** IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
** CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
** TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
** MATERIALS OR THE USE OR OTHER DEALINGS IN THE MATERIALS. 
*/ 
/* Platform-specific types and definitions for egl.h 
* $Revision: 1.2 $ on $Date: 2011/07/26 23:17:28 $ 
* 
* Adopters may modify khrplatform.h and this file to suit their platform. 
* You are encouraged to submit all modifications to the Khronos group so that 
* they can be included in future versions of this file. Please submit changes 
* by sending them to the public Khronos Bugzilla (http://khronos.org/bugzilla) 
* by filing a bug against product "EGL" component "Registry". 
*/ 
/* 
* This document is licensed under the SGI Free Software B License Version 
* 2.0. For details, see http://oss.sgi.com/projects/FreeB/ . 
*/ 
/* Platform-specific types and definitions for OpenGL ES 1.X gl.h 
* Last modified on 2008/12/19 
* 
* Adopters may modify khrplatform.h and this file to suit their platform. 
* You are encouraged to submit all modifications to the Khronos group so that 
* they can be included in future versions of this file. Please submit changes 
* by sending them to the public Khronos Bugzilla (http://khronos.org/bugzilla) 
* by filing a bug against product "OpenGL-ES" component "Registry". 
*/ 
/ * File: fpcomp.c 
* 
* Purpose: Sample parser for ARB_fragment_program 
* 
* 
* Author: Benj Lipchak, ATI Research 
* 
* Based on ARB_vertex_program sample 
* implementation from NVIDIA 
* 
* Copyright: Copyright (c) 2002 ATI Technologies Inc 
* 
* Use of this sample code is subject to the terms and conditions of the 
* ATI Technologies Inc. Software Development Kit License Agreement. 
* If you have not accepted and agreed to this License, you have no 
* rights to use the software contained herein. 
*/ 
/* 
** Copyright (C) 2002, NVIDIA Corporation. 
** 
** NVIDIA Corporation("NVIDIA") supplies this software to you in consideration 
** of your agreement to the following terms, and your use, installation, 
** modification or redistribution of this NVIDIA software constitutes 
** acceptance of these terms. If you do not agree with these terms, please do 
** not use, install, modify or redistribute this NVIDIA software. 
** 
** In consideration of your agreement to abide by the following terms, and 
** subject to these terms, NVIDIA grants you a personal, non-exclusive 
** license, under NVIDIA's copyrights in this original NVIDIA software (the 
** "NVIDIA Software"), to use, reproduce, modify and redistribute the NVIDIA 
** Software, with or without modifications, in source and/or binary forms; 
** provided that if you redistribute the NVIDIA Software, you must retain the 
** copyright notice of NVIDIA, this notice and the following text and 
** disclaimers in all such redistributions of the NVIDIA Software. Neither the 
** name, trademarks, service marks nor logos of NVIDIA Corporation may be used 
** to endorse or promote products derived from the NVIDIA Software without 
** specific prior written permission from NVIDIA. Except as expressly stated 
** in this notice, no other rights or licenses express or implied, are granted 
** by NVIDIA herein, including but not limited to any patent rights that may 
** be infringed by your derivative works or by other works in which the NVIDIA 
** Software may be incorporated. No hardware is licensed hereunder. 
** 
** The NVIDIA Software is provided by NVIDIA on an "AS IS" BASIS, WITHOUT 
** WARRANTIES OR CONDITIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING 
** WITHOUT LIMITATION WARRANTIES OR CONDITIONS OF TITLE, NON-INFRINGEMENT, 
** MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE, REGARDING THE NVIDIA 
** SOFTWARE OR ITS USE AND OPERATION ALONE OR IN COMBINATION WITH YOUR 
** PRODUCTS. 
** 
** IN NO EVENT SHALL NVIDIA BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL, 
** SPECIAL, EXEMPLARY OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
** LOST PROFITS; PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, 
** DATA, OR PROFITS; OR BUSINESS INTERRUPTION) ARISING IN ANY WAY OUT OF THE 
** USE, REPRODUCTION, MODIFICATION AND/OR DISTRIBUTION OF THE NVIDIA SOFTWARE, 
** HOWEVER CAUSED, AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING 
** NEGLIGENCE), STRICT LIABILITY OR OTHERWISE, EVEN IF NVIDIA HAS BEEN ADVISED 
** OF THE POSSIBILITY OF SUCH DAMAGE.* 
/* A Bison parser, made by GNU Bison 2.3. */ 
/* Skeleton interface for Bison's Yacc-like parsers in C 
Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006 
Free Software Foundation, Inc. 
This program is free software; you can redistribute it and/or modify 
it under the terms of the GNU General Public License as published by 
the Free Software Foundation; either version 2, or (at your option) 
any later version. 
This program is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
GNU General Public License for more details. 
You should have received a copy of the GNU General Public License 
along with this program; if not, write to the Free Software 
Foundation, Inc., 51 Franklin Street, Fifth Floor, 
Boston, MA 02110-1301, USA. */ 
/* As a special exception, you may create a larger work that contains 
part or all of the Bison parser skeleton and distribute that work 
under terms of your choice, so long as that work isn't itself a 
parser generator using the skeleton or a modified version thereof 
as a parser skeleton. Alternatively, if you modify or redistribute 
the parser skeleton itself, you may (at your option) remove this 
special exception, which will cause the skeleton and the resulting 
Bison output files to be licensed under the GNU General Public 
License without this special exception. 
This special exception was added by the Free Software Foundation in 
version 2.2 of Bison. */ 
/************************************************************************** 
* 
* Copyright 2006 Tungsten Graphics, Inc., Bismarck, ND. USA. 
* All Rights Reserved. 
* 
* Permission is hereby granted, free of charge, to any person obtaining a 
* copy of this software and associated documentation files (the 
* "Software"), to deal in the Software without restriction, including 
* without limitation the rights to use, copy, modify, merge, publish, 
* distribute, sub license, and/or sell copies of the Software, and to 
* permit persons to whom the Software is furnished to do so, subject to 
* the following conditions: 
* 
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
* FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL 
* THE COPYRIGHT HOLDERS, AUTHORS AND/OR ITS SUPPLIERS BE LIABLE FOR ANY CLAIM, 
* DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
* OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE 
* USE OR OTHER DEALINGS IN THE SOFTWARE. 
*The above copyright notice and this permission notice (including the 
* next paragraph) shall be included in all copies or substantial portions 
* of the Software. 
* 
* 
**************************************************************************/ 
/* 
* Copyright © 2007 Red Hat, Inc. 
* 
* Permission is hereby granted, free of charge, to any person obtaining a 
* copy of this software and associated documentation files (the "Software"), 
* to deal in the Software without restriction, including without limitation 
* the rights to use, copy, modify, merge, publish, distribute, sublicense, 
* and/or sell copies of the Software, and to permit persons to whom the 
* Software is furnished to do so, subject to the following conditions: 
* 
* The above copyright notice and this permission notice (including the next 
* paragraph) shall be included in all copies or substantial portions of the 
* Software. 
* 
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
* THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
* OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
* SOFTWARE. 
* 
* Authors: 
* Dave Airlie <airlied@redhat.com>

/*
 * Copyright © 2008 Kristian Høgsberg
 *
 * Permission to use, copy, modify, distribute, and sell this software and its
 * documentation for any purpose is hereby granted without fee, provided that
 * the above copyright notice appear in all copies and that both that copyright
 * notice and this permission notice appear in supporting documentation, and
 * that the name of the copyright holders not be used in advertising or
 * publicity pertaining to distribution of the software without specific,
 * written prior permission.  The copyright holders make no representations
 * about the suitability of this software for any purpose.  It is provided "as
 * is" without express or implied warranty.
 *
 * THE COPYRIGHT HOLDERS DISCLAIM ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
 * INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO
 * EVENT SHALL THE COPYRIGHT HOLDERS BE LIABLE FOR ANY SPECIAL, INDIRECT OR
 * CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
 * DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
 * TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE
 * OF THIS SOFTWARE.
 */

