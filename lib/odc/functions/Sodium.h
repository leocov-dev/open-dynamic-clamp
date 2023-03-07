/*
Copyright 2017. Niraj S. Desai, Richard Gray, and Daniel Johnston.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
*/

// A fast, transient Na+ conductance using the Hodgkin-Huxley formalism.
// For speed, the parameters alphaM, betaM, alphaH, and betaH are pre-calculated
// and put in lookup tables stored as global variables.

#include "generated_luts.h"

// At every time step, calculate the sodium current in the Hodgkin-Huxley manner
float Sodium(float v) {
    static float mNaVar = 0.0;    // activation gate
    static float hNaVar = 1.0;    // inactivation gate
    float v10 = v * 10.0;
    int vIdx = (int) v10 + 1000;
    vIdx = constrain(vIdx, 0, 1500);
    mNaVar = mNaVar + msecs * (alphaM[vIdx] * (1 - mNaVar) - betaM[vIdx] * mNaVar);
    if (mNaVar < 0.0) mNaVar = 0.0;
    hNaVar = hNaVar + msecs * (alphaH[vIdx] * (1 - hNaVar) - betaH[vIdx] * hNaVar);
    if (hNaVar < 0.0) hNaVar = 0.0;
    float current1 = -conducts[2] * mNaVar * mNaVar * mNaVar * hNaVar * (v - 50);  // ENa = +50 mV
    return current1;
}

