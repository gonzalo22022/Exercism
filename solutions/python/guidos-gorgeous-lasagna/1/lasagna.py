EXPECTED_BAKE_TIME= 40
time_remaining = 30
number_of_layer= 5
def bake_time_remaining(time_remaining):
    """Calculate time of remaing"""
    time = EXPECTED_BAKE_TIME - time_remaining
    
    return time


def preparation_time_in_minutes(number_of_layers):
    """Calculate time for layers"""
    number_of_layers = number_of_layers * 2
    return number_of_layers    

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    total = number_of_layers *2 + elapsed_bake_time
    return total

elapsed_time_in_minutes(3, 20)
