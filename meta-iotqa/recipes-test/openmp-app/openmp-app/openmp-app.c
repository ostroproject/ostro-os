/*
 * Copyright (C) 2016 Intel Corporation
 *
 * Contact: Jussi Laako <jussi.laako@linux.intel.com>
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to
 * deal in the Software without restriction, including without limitation the
 * rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
 * sell copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 * IN THE SOFTWARE.
 */

#include <stdio.h>
#include <omp.h>

int main ()
{
	int i;
	int r = 0;
	static const int N = 4096;
	int x[N];

	printf("Number of threads in the pool: %d\n", omp_get_max_threads());
	printf("Number of processors: %d\n", omp_get_num_procs());

	puts("Running test loop...");
#	pragma omp parallel for schedule(dynamic)
	for (i = 0; i < N; i++)
	{
		x[i] = N / 2 - i;
	}
	puts("...done - verifying...");
	for (i = 0; i < N; i++)
	{
		if (x[i] != (N / 2 - i))
		{
			printf("Failure on index %d\n", i);
			r = -1;
		}
	}
	if (!r) puts("OK");

	return r;
}

