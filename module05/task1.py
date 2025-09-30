################################################################################################
##### Vectorize the power computing function ##################################################
################################################################################################

# In this script we will build a vectorized power function using arrays

# We import numphy
import numpy as np

#We define a function that calculates the power based on specification but for different vind speeds V
def power_calc(p_rated=15, v_in = 3, v_ratd = 11, v_out = 25, interpol = "linear"):
    """We define a function which calculates power output based on user inputs"""

    # We check for error in user input 
    inputs = {'p_rated': p_rated, 'v_in': v_in, 'v_ratd': v_ratd, 'v_out': v_out}

    for name, value in inputs.items():
        if not isinstance(value, (int, float)): 
            raise ValueError(f"Invalid input: {value} is not a number")  
    
    if not interpol == "linear" or interpol == "cubic":
        raise ValueError(f"Invalid input: {interpol}. Interpolation should be either 'linear' or 'cubic'.")  
    
    #Wind Speed Vector
    v=np.array([5.0, 10.0, 12.0 , 15.0, 22.0])

    #We make a variable that count the number of different wind speeds in the wind speed vector
    v_size = v.size

    #We make a horizontal vector that can be used to vectorize the user input data:
    ones_vector = np.ones(v_size).reshape(1, v_size)

    # We vectorize the user input
    p_rated = p_rated * ones_vector
    v_in = v_in * ones_vector
    v_ratd = v_ratd * ones_vector
    v_out = v_out * ones_vector

    #We calculate g based on whether the power curve is assumed to be linear or cubic
    if interpol == "linear":
        g = (v-v_in)/(v_ratd-v_in)
    elif interpol == "cubic":
        g = v**3/v_ratd**3

    # We calculate the power output P(v)
    p = np.where(
        (v < v_in) | (v >= v_out), g * 0,
        np.where((v >= v_in) & (v < v_ratd),g * p_rated,
            np.where((v_ratd <= v) & (v < v_out), p_rated,
                0 
            )))
        
    return v, p

#We use the function to calculate and print the power output
if __name__ == '__main__':
    # We call the power output function to calculate power output based on user defined inputs:
    wind, power = power_calc(15, 3, 11, 25, "linear")

    #Make sure we are working with flat arays so we can print the results:
    wind = np.ravel(wind)
    power = np.ravel(power)

    # We print the calculated power output: 
    for w, p in zip(wind, power):
        print(f"Wind Speed: {w:.2f} m/s → Power Output: {p:.2f} MW")