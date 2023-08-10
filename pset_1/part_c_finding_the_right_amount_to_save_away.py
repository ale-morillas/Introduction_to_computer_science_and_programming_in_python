# THE SOLUTION TO PART C OF PROBLEM SET ONE

#initial annual salary to save the starting value
initial_a_s = 120000
#annual Salary
a_s = initial_a_s
total_cost = 1000000.0 
#annual return
r = 0.04
#semi annual raise
s_a_r = 0.07 # nest time get it from the user
#portion down payment
portion_d_p = 250000.0 #total_cost * 0.25
low = 0.0
high = 1.0
#guess
g = (low + high ) / 2
#monthly_salary saved
m_s_s = (initial_a_s / 12) * g
#current savings
current_sv = 0.0
#months
m = 0
#Number Of Guesses
NoOfGs = 0
if ((3 * initial_a_s ) + (initial_a_s* r)) <= portion_d_p:
    print('It is not possible to pay the down payment in three years.')
else:
    while abs(current_sv - portion_d_p) > 100:
        current_sv = 0.0
        #Ver cuanto tengo ahorrado en 36 meses con el % de mi salario que ahorro todos los meses (g).
        while m < 36:
            if ((m - 1)%6 == 0) and (m != 1):
                a_s = a_s + (a_s * s_a_r)
                m_s_s = (a_s/12) * g
            current_sv = current_sv + (current_sv * (r/12)) + m_s_s
            m = m + 1
        NoOfGs = NoOfGs + 1
        a_s = initial_a_s
        m = 0
        #Si lo que tengo ahorrado menos el portion down payment es mayor que 100, g se queda corta. Si es mayor, g se pasa.
        if abs(current_sv - portion_d_p) > 100:
            if current_sv > portion_d_p:
                high = g
            else:
                low = g
            g = (high + low) /2
            m_s_s = (initial_a_s / 12) * g
        #Si mis ahorros menos el portion down payment es menor que 100, g es correcta.
        else:
            print('Best savings rate:', round(g, 4))
            print('Steps in bisection search:', NoOfGs)
            break