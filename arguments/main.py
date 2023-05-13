# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


# Part #1


def greet(name, greet_temp = "Hello, <name>!"):
    
    return greet_temp.replace('<name>', name)


print(greet('Bugs Bunny'))
print(greet('Doc', "Eh... What's up, <name>!"))


# Part #2


def force(mass, body="earth"):
    gravity_factors = {
        "mercury": 3.7,
        "venus": 8.9,
        "earth": 9.8,
        "moon": 1.6,
        "mars": 3.7,
        "jupiter": 23.1,
        "saturn": 9.0,
        "uranus": 8.7,
        "neptune": 11.0,
        "pluto": 0.7
    }

    # if body not in gravity_factors:
    #     return(f"This Celestial body:{body}, is not in the list")

    gravity_round = round(gravity_factors[body], 1)
    # print(gravity_round)
    force = round(mass * gravity_round, 1)
    # print(force)

    return force

print(force(50.0, "moon"))


# Part #3


def pull(mass_1, mass_2, distance):
    force = (6.674 * 10**-11) * ((mass_1 * mass_2) / distance**2)

    return force

print(round(pull(800, 1500, 3), 10))