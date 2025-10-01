"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    letras = ['A','B','C','D',]
    for i in range(number):
        yield letras[i%4]

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    letras = ['A','B','C','D',]
    row = 1
    cont= 0
    while cont < number:
        if row == 13:
            row += 1
            continue
        for letra in letras:
            if cont >= number:
                break
            yield f'{row}{letra}'
            cont += 1
        row += 1
        
def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    letras = ['A','B','C','D',]
    asignaciones = {}
    row = 1
    seat_index= 0

    for pasajero in passengers:
        if row == 13:
            row +=1
        letra = letras[seat_index % 4]
        asignaciones[pasajero]= f'{row}{letra}'
        seat_index += 1
        if seat_index %4 == 0:
            row +=1

    return asignaciones
            
        

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        code = f'{seat}{flight_id}000'
        yield code[:12]
