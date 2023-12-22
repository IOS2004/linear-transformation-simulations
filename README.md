# VESMOS 
#### Video Demo:  <[Click here](https://youtu.be/b8lJ9V0CyXQ?si=Q8DyO2LZtKxi72P1)>
#### Description:  A visual tool for Linear Algebra conceptual and intuitive understanding.
> ## NON-TECHNICAL INFO
## INTRODUCTION
Vesmos is a mathematical tool for linear algebra in 2D. Vesmos is mainly focused on vectors and matrices. More so than actual computational help which is trivial and commonly available, Vesmos focuses on enhancing intuitive learning. Vesmos explains abstract concepts of linear algebra in visual aspects and allows users to visualize what they are learning and what is its significance. 
>Vesmos aims to make linear algebra more interesting and interactive.

Vesmos includes an intractable graph and various sections dedicated to the fundamental concepts of linear algebra. They are Vector addition and subtraction, dot product, Linear transformation, Eigen values and vectors, Determinants and Diagonalization.
Each section provides visualization tools for their respective headings. The user can input values of matrices / vectors and submit it to view visual aspect of the same in accordance with section heading. You can use your textbook examples and aspect accurate solution. Vesmos is mathematically accurate and covers edge cases.
Vesmos is expected to be used in supplement with linear algebra courses and not to be used for learning concepts but only to strengthen the already-learned topics.
This tool is best benefited with lectures of [3Blue1Brown](https://www.youtube.com/@3blue1brown) on linear algebra.

Vesmos provides user friendly interface which is intuitive to follow. It includes various features such as light/dark mode, resizable screen, zoom able and drag-gable graph.

_NOTE Only 2 tuple Vectors and 2 x 2 Matrix inputs is allowed as Vesmos deals with 2 dimensions only._

## Features
As mentioned before Vesmos Software is divided into 6 sections. I will explain each sections in brief below.

### Vector Addition and Subtraction
This is simplest of all section and does exactly what it says. It is beneficial as it gets you familiar with fundamental working of vectors which is crucial for linear algebra. Although trivial it can be useful for users who are new to Linear algebra. 

### Dot Product
Dot product is one of simplest and fundamental concept in algebra in the above section Vesmos tries to provide a intuitive understanding what actually happening behind the scenes of dot product. It works on the principle of how vector can be interpreted as 1x2 matrix and matrix is essentially a linear transformation, hence in this section we see linear transformation due to first vector and the effect due to this in second vector which essentially results in magnitude of dot product.

$$
\left(\begin{array}{cc} 
A & B \\
\end{array}\right)
\left(\begin{array}{cc} 
C \\ 
D
\end{array}\right)
$$  


This expression equates to dot product. Here Vector 1 is used to linearly transform original grid. This operation is same as 

$$ T(x) = Ax $$ 

where A is Vector 1, x is Vector 2 and Ax is transformed Vector 2 which whose magnitude indicates dot product.

### Linear transformation
In a visual way Linear transformation is showed by change of basis via provided matrix (standard basis are (1, 0) and (0, 1)). Each of the column of matrix is used as a new basis for transformed graph. This section also provides vector input to visualize how vector transforms along with graph. Transformed vector can be calculated as 

$$ V =
\left(\begin{array}{cc} 
A & B \\
C & D
\end{array}\right)
\left(\begin{array}{cc} 
E \\ 
F
\end{array}\right)
$$ 

Where first multiple is 2x2 matrix and second is original vector. 

### Eigen Value and Vectors
After linear transformation vector which are scaled and not rotated are called eigen vectors and by the value it is scaled is called eigen value. This section calculates Eigen values and vectors for inputted matrix and also shows the eigen vector span in graph. Eigen vector can also be verified by using linear transformation section.

### Determinants
Determinant of a matrix can be visualized as a scaling factor of a grid square which is scaled due to transformation by that matrix. This section highlights that square. As object of any shape can be made using small squares essentially determinant is scale by which transformed graph area is increased w.r.t original graph.

### Diagonalization
This is one of the most crucial topic in Linear Algebra which reduces the computation of matrices by great extent. This section helps to visualize the process by which matrix is diagonalized (if diagonalizable) and also calculates diagonalized matrix.

> ## TECHNICAL INFO
### Requirements
Python version 3.9, pygame, pygame_gui, math.

### Languages
Python

### Installation
Python project is compiled into single executable using pyinstaller, *images folder should be in same directory as .exe file for proper working.*
***For downloading open [Realease tab](https://github.com/IOS2004/linear-transformation-simulations/releases/tag/v1.0.0.0) and download Vesmos.rar from assets section. Extract it and you are all ready to go.***

### Working
main.py and functions.py includes all the code for software functioning. main.py contains primary code and main game loop while functions.py contains helper functions for screen surfaces.

Files can be found in [Github Repository](https://github.com/IOS2004/linear-transformation-simulations)

#### Graph 
Graph was built using pygame drawing functions of line and aaline. From origin x and y axis are drawn, these axis are basis dependent i.e was built such that they point to the direction of provided basis vectors which by default are (1, 0) and (0, 1). Parallel to these axis grid lines are drawn. Reference grids are always parallel to standard axis. Spacing between grid lines is constant. By altering the origin position and spacing dragging and zooming is possible for that purpose axis are drawn in two parts each starting from origin. By changing basis vectors we can achieve linear transformation.

original coordinate system of screen is converted to graph coordinate system to perform operations necessary.
Graph is updated 60 frames per second.

#### Vectors
Vector are drawn using function draw_bvector() function which draws the line from origin to given vector coordinates. This vector is first multiplied by basis matrix to get transformed vector then it is drawn.
Vector also include arrow triangle which is drawn using pygame.draw.polygon() function

#### Screen surfaces
There are three main screen surface: front page, graph, side menu. 
Side menu contains 7 pages in which the first one contains six buttons for each section heading. Each section contains input boxes output text, reset and submit buttons. Side menu can be toggled or de-toggle using toggle button on top right. Dark mode and light mode is built by changing the color of graph and side menu surfaces.
Buttons were made using button class present in functions.py. Input boxes are built using pygame_gui.

#### Side menu sections
Each section has it's unique functioning hence is divided in 6 boolean s in main game loop i.e. page2 to page7 where page1 contains button to access these sections. Graph is modified by taking the inputted value through side menu and performing valid operations to output appropriate results. Reset button is used to reset all the inputted variables and section variables. Input boxes are reused across sections by cleaning them via kill function and re initialization.

#### Responsiveness and resize-ablity
Screen is resizable but there is minimum limit for width and height so as the screen elements remain in proper place without getting jumbled.

#### User interface
Pygame_gui is used in building input boxes only. Buttons and other ui elements are built without it because I found about this module little later in course of development.

#### Invalid inputs
Software handles all the invalid inputs like blank input, character input, expression input and displays invalid input warning.

### Acknowledgements
*David Malan* and all the CS50 staff.                                                                                                                                            
*Grant Sanderson* from [3Blue1Brown](https://www.youtube.com/@3blue1brown).
