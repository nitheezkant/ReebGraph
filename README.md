
# An attempt from scratch to generate Reeb Graph




## Functionality
The goal of this code was to generate reem graphs of complexes, from scratch without using any already excisting topology code. However, given the technical and time constraints we have acchived the following.

### Given a triangulation of any complex


- From any given triangulation of a complex, the code is capable of plotting the complex and identifing the maximas, minimas, saddles and regular points. This is done by analising the link of each point. This part is of the code is fully implemented.

- Further, the code tries to generate an approximate Reeb graph by removing all the regular points one by one and connecting any 2 critical points it touches. This of course contains edges that should not be a part of the reeb graph. This is why this is an approximation and a robust algorithm should be applied later to connect the critical points correctly. However, even when there are redundent edges, the code is fully accurate about the vertices in the reeb graph.

### Given parametric equation of the complex

- From any given parameterisation of a complex, the code is capable of finding the critical points. This is done by traditional method of deffentiating and equating to zero and then solving the equations. This part of the code is fully implimented.

- The next task is to connect the critical points to get the reeb graph. This task is not implimented. 


## Instructions To Run 
### Requirements 
- Python 3.8 and above
- numpy 
- matPlotLib
- sympy
### Triangulation of complex method 
Triangulate the complex and then enter it into the ```Input_Points.txt``` file in the given format(text indicated with ```//``` is for instruction and should NOT be included in the txt file).
```
1 0 0 0 //Point number(1), follwed by x, y and z coordinates(all integer).
2 3 5 7 //Points to which 1 is connected through edges(Neighbourhood points).
2 1 2 4 //Point number(2), follwed by x, y and z coordinates.
1 3 5   //Points to which 2 is connected, note: if 1 is connected to 2, it should be mentioned that 2 is also connected to 1.
3 1 4 5 //Point number(7), follwed by x, y and z coordinates.
1 2 5.  //The neighbourhood should be mentioned in eaither clockwise or anti clockwise manner
4 4 4 1
1 5 6 7
5 2 3 3
3 1 2 4
6 4 4 8
4
7 -1 -1 -1
1 4      //Continue till the last point.
x        // Use 'x' to indicate end of file.
```
The above input represents this complex given in 


![App Screenshot](https://github.com/nitheezkant/hosting/blob/main/Example%201.png)

Note: z coordinate is taken as the height function.
Then, on terminal run 
``` bash
python3 main.py
```
Enter choice 1, and then press any charecter and click enter.\
This will generate 2 graphs, 1st one is the simplex and second one is the approximate reeb graph along with the critical points marked in colors mentioned in the legend.

### Parametric equation of complex method

Then, on terminal run 
``` bash
python3 main.py
```
Enter choice 2.

Now if you can type 1 for your custom function, or 2 for inbuilt torus or 3 for inbuilt sphere.\
Uncomment the code given under if ```ch==1``` to enter your own paramentric function and run the code with ch 1 for custom funtion.\
Note, by entering the function directly in the code, the user can properly get error statements in case the format of the equation was wrong. Taking user input here was a big challenge, as converting string to sympy expression caused many unexpected errors.

For inbult complexes, just use ch 2 or 3.

In all cases, you will see a plot with the critical points on it the output. In case of inbuilt functions, you will also see the complex.\
Connecting these critical points appropriately should give the reeb graph, however due to challenges, this task has not been implemented.\
Note: Z axis is taken as height function.







## Screenshots

### Triangulation of complex method 

Output of  ```example1.txt```


![App Screenshot](https://github.com/nitheezkant/hosting/blob/main/Screenshot%202023-05-15%20at%201.32.56%20PM.png)



Output of  ```example2.txt```


![App Screenshot](https://github.com/nitheezkant/hosting/blob/main/Screenshot%202023-05-15%20at%201.33.45%20PM.png)



### Parametric equation of complex method 

Output of inbuilt torus


![App Screenshot](https://github.com/nitheezkant/hosting/blob/main/Torus.png)



Output of  inbuilt sphere

![App Screenshot](https://github.com/nitheezkant/hosting/blob/main/sphere.png)


```Sample_Outputs``` contains all of these png files.




## References 

 - [Topology Matching for Fully Automatic Similarity Estimation of 3D Shapes](https://graphics.stanford.edu/courses/cs468-08-fall/pdf/Hilaga01.pdf)
 - [Computing Reeb Graphs as a Union of Contour Trees, paper by Vijay Natarajan](https://vgl.csa.iisc.ac.in/pdf/pub/reeb_contour_paper.pdf)
 - Lecture slides of Prof Amit Chattopadhyay
 

## A project by 

- [Nitheezkant R](https://www.github.com/nitheezkant)
- [Nilay Prabodh Kamat](https://www.github.com/Nilsiloid)

