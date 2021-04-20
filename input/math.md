# Math

The mathematics part of the library contains various functionality including but not limited to linear algebra, constants, geometry and more! It aims to provide generic class representations of mathematical objects such as shapes and custom containers like vectors and matrices not seen in the standard library.

## Features
**Matrices**
- Can create NxM matrices of type T.
- Supports row and column major ordering for matrices. 
- Can be managed using fixed or dynamic memory management, and work together. 
- Matrix Arithmetic operations can be performed between varying types of matrices. (e.g. dynamic 4x3 integer matrix multiplied by a fixed 3x4 real matrix)#

**Vectors**
- Can create N-dimensional vectors of type T 
- Can and can be managed using fixed or dynamic memory management. 
- Arithmetic and comparison operations can be performed between varying types and dimensions of vectors. (e.g. a vector4 multiplied by a vector2)

**Other**
- Can create Quarternions of type T (Fixed as quarternions have a fixed number of components - x,y,w,z)
- Contains basic structures for geometrical structures like rays, segments and lines.
- Contains basic random number generation for a variety of arithmetic types.
