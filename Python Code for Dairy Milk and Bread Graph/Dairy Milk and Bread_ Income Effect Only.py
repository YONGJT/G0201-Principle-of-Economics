import matplotlib.pyplot as plt
import numpy as np
import matplotlib.axes as ax
import matplotlib.colors as mcolors



# Marker for intersection points
def labelhorizontal_plot(x1,x2,y):
    a1 = [x1,x2]
    a2 = [y,y]
    plt.plot(a1,a2,'--',color='black',linewidth=1.5)
def labelvertical_plot(x,y1,y2):
    a1 = [x,x]
    a2 = [y1,y2]
    plt.plot(a1,a2,'--',color='black',linewidth=1.5)

arrow_x = 0  # X-coordinate where the arrow will point
arrow_y = (-np.pi/2)  # Y-coordinate corresponding to the line at that x
def arrowS(arrow_xa,arrow_ya,arrow_xb,arrow_yb):
    plt.annotate(
        '',  # No text for the annotation
        xy=(arrow_xb, arrow_yb),  # Arrow's tip location
        xytext=(arrow_xa, arrow_ya),  # Start point of the arrow
        arrowprops=dict(
            arrowstyle='->',  # Arrow style
            color='green',       # Arrow color
            lw=2.5,               # Arrow line width
        )
    )
def arrowD(arrow_xa,arrow_ya,arrow_xb,arrow_yb):
    plt.annotate(
        '',  # No text for the annotation
        xy=(arrow_xb, arrow_yb),  # Arrow's tip location
        xytext=(arrow_xa, arrow_ya),  # Start point of the arrow
        arrowprops=dict(
            arrowstyle='-|>',  # Arrow style
            color='green',       # Arrow color
            lw=2.5,               # Arrow line width
        )
    )

def arrowI(arrow_xa,arrow_ya,arrow_xb,arrow_yb):
    plt.annotate(
        '',  # No text for the annotation
        xy=(arrow_xb, arrow_yb),  # Arrow's tip location
        xytext=(arrow_xa, arrow_ya),  # Start point of the arrow
        arrowprops=dict(
            arrowstyle='->',  # Arrow style
            color='red',       # Arrow color
            lw=2.5,               # Arrow line width
        )
    )
def arrowE(arrow_xa,arrow_ya,arrow_xb,arrow_yb):
    plt.annotate(
        '',  # No text for the annotation
        xy=(arrow_xb, arrow_yb),  # Arrow's tip location
        xytext=(arrow_xa, arrow_ya),  # Start point of the arrow
        arrowprops=dict(
            arrowstyle='-|>',  # Arrow style
            color='red',       # Arrow color
            lw=2.5,               # Arrow line width
        )
    )

 
# Functions of Graphs
def budget_line(p1, p2, income, x_max):
    x = np.linspace(0, x_max, 100)
    y = (income - p1 * x) / p2
    return x, y
def indifference_curve(a,b,u, x_max):
    x = np.linspace(0.1, x_max, 50000)  # Avoid division by zero
    y = (u / (x**a))**(1/b)
    return x, y
def income(x0,y0,px,py):
    return x0*px +y0*py
def alpha(x0,y0,px,py):
    return (x0*px)/(y0*py)
def B(alpha):
    return 1/(1+alpha)
def A(b,alpha):
    return alpha*b
def Utility(x0,y0,a,b):
    return ((x0)**a)*((y0)**b)

# Defining Variables
x0 = 1.28
y0 = 0.5556
px = 19.2
py = 163.08

#######################################
alpha0 = alpha(x0,y0,px,py)
b0 = B(alpha0)
a0 = A(b0,alpha0)
Income = income(x0,y0,px,py)
#######################################

# Figures
plt.figure(figsize=(10, 6))
xextraticks = []
yextraticks = []
"""
#Actual Budget Line
x,y = budget_line(px,py,Income,60)
plt.plot(x,y, label="Initial Budget Constraint", color="orange",linestyle="-",linewidth=2.5)
"""
#Actual Indifference_curve
x, y = indifference_curve(a0,b0,Utility(x0,y0,a0,b0), 150)
plt.plot(x, y, label="Initial Indifference Curve", color="blue", linestyle="-", linewidth=0.8)
"""
#Intersection point of actual budget line and Actual indifference curve 
#x0,y0 = intersection(income,Ucal(income,px,py),px,py)
plt.plot(x0,y0,marker='o',color="black",markersize=10)
labelhorizontal_plot(0,x0,y0)
labelvertical_plot(x0,0,y0)
xextraticks.append(x0)
yextraticks.append(y0)"""
######################################################################################################################################################################
px1 = 16.2
py1 = 163.08
x1 = x0*((px/px1)**(b0/(a0+b0))) 
y1 = y0*((px/px1)**(-a0/(a0+b0)))
compensatedIncome = income(x1,y1,px1,py1)

#Compensated Budget Line
x,y = budget_line(px1,py1,compensatedIncome,60)
plt.plot(x,y, label="Compensated Budget Constraint", color="orange",linestyle=":",linewidth=1.8)

#Compensated Indifference_curve
#x, y = indifference_curve(a0,b0,Utility(x0,y0,a0,b0), 150)
#plt.plot(x, y, label="Indifference Curve 2023", color="blue", linestyle="-", linewidth=0.8)

#Intersection point of actual budget line and Actual indifference curve 
#x0,y0 = intersection(income,Ucal(income,px,py),px,py)
plt.plot(x1,y1,marker='o',color="black",markersize=10)
labelhorizontal_plot(0,x1,y1)
labelvertical_plot(x1,0,y1)
xextraticks.append(x1)
yextraticks.append(y1)
"""
#Arrow of Substitution effect
arrowS(x0,y0,x1,y1)
arrowD(0,y0,0,y1)
arrowD(x0,0,x1,0)
plt.text(x0+0.09,0,"Substitution\nEffect",color='green',fontname='Times New Roman',fontsize=12,weight='bold',horizontalalignment='center',verticalalignment='bottom')"""
######################################################################################################################################################################
# Income Effect
px2 = 16.2
py2 = 163.08
x2 = a0*Income/px2
y2 = b0*Income/py2

#Final Budget Line
x,y = budget_line(px2,py2,Income,60)
plt.plot(x,y, label="Final Budget Constraint", color="Brown",linestyle="-",linewidth=3.5)

#Final Indifference_curve
x, y = indifference_curve(a0,b0,Utility(x2,y2,a0,b0), 150)
plt.plot(x, y, label="Final Indifference Curve", color="blue", linestyle="-",linewidth=2.5)

#Intersection point of compensated budget line and Actual indifference curve 
#x0,y0 = intersection(income,Ucal(income,px2,py2),px2,py2)
plt.plot(x2,y2,marker='o',color="black",markersize=10)
labelhorizontal_plot(0,x2,y2)
labelvertical_plot(x2,0,y2)
xextraticks.append(x2)
yextraticks.append(y2)

#Arrow of Income effect
arrowI(x1,y1,x2,y2)
arrowE(0.05,y1,0.05,y2)
arrowE(x1,0,x2,0)
plt.text(x2-0.025,0,"Income\nEffect",color='red',fontname='Times New Roman',fontsize=12,weight='bold',horizontalalignment='center',verticalalignment='bottom')
######################################################################################################################################################################
#Ticks at both axes
xticks = list(range(0,2,5)) + xextraticks
yticks = list(range(0,8,5)) + yextraticks
plt.xticks(xticks,fontsize=14)
plt.yticks(yticks,fontsize=14)

## Setting of graphs
plt.xlabel("Quantity of Class I Fluid Beverage Milk (cwt)",fontname='Times New Roman',fontsize=18)
plt.ylabel("Quantity of Bread (cwt)",fontname='Times New Roman',fontsize=18)
plt.title("Income Effect \nfor Class I Fluid Beverage Milk and Bread",fontname='Times New Roman',fontsize=24)

#Label Points
#plt.text(x0-0.004,y0-0.024,"A",color='Black',fontname='Times New Roman',fontsize=18,weight='bold',horizontalalignment='right',verticalalignment='bottom')
plt.text(x1-0.004,y1-0.04,"B",color='Black',fontname='Times New Roman',fontsize=18,weight='bold',horizontalalignment='right',verticalalignment='bottom')
plt.text(x2+0.002,y2+0.002,"C",color='Black',fontname='Times New Roman',fontsize=18,weight='bold',horizontalalignment='center',verticalalignment='bottom')

plt.legend()
plt.grid(False)
plt.xlim(0, 8)
plt.ylim(0, 1)
plt.show()