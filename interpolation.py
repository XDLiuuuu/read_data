#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##Interpolation for the imaginary part of the permitivity for the MoS_2.
##The procedurte is similar as before.
a2 =[1.54665, 1.588, 1.62809, 1.66493, 1.70959, 1.75495, 1.78146, 1.80499, 1.82014, 1.83011, 1.83853, 1.84654, 1.86032, 1.869, 1.89185, 1.90386, 1.91474, 1.9294, 1.95811, 1.9776, 1.99673, 2.01711, 2.03736, 2.05652, 2.07334, 2.09582, 2.12997, 2.17017, 2.21468, 2.29297, 2.37477, 2.44997, 2.51869, 2.57735, 2.62608, 2.67149, 2.7101, 2.72915, 2.74539, 2.78068, 2.81597, 2.8358, 2.86125, 2.88565, 2.91518, 2.92859, 2.95268, 2.97141, 2.98992, 3.01423]

b2 =[0.951, 0.911, 1.033, 0.945, 1.257, 1.589, 2.751, 3.678, 5.955, 7.465, 9.313, 10.905, 12.669, 13.456, 11.935, 11.374, 10.503, 9.784, 11.336, 12.582, 14.399, 15.032, 14.23, 12.261, 11.114, 9.224, 8.685, 8.198, 8.485, 9.132, 10.057, 11.409, 13.467, 15.814, 18.73, 21.788, 24.851, 26.209, 28.057, 31.263, 34.469, 35.78, 37.247, 37.426, 36.52, 36.075, 34.281, 33.095, 31.423, 30.114]
pl.plot(a2,b2,"ro")

for kind in ["cubic"]:#The interpolation method is "Cubic method".
    
    f2=interpolate.interp1d(a2,b2,fill_value="extrapolate")      #Define a function f2, for the imaginary part.
    # ‘slinear’, ‘quadratic’ and ‘cubic’ refer to a spline interpolation of first, second or third order)
    xnew=a2
    ynew=f2(a2)
    pl.plot(xnew,ynew,label=str(kind))
pl.legend(loc="lower right")
plt.xlabel('E(in eV)')
plt.title('imaginary part of permitivity for MoS2')
pl.show()

