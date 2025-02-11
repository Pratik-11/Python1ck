values = ('275', True, 'abracadabra', 100) #('275', True, 'abracadabra', 100) 
print(values)
values = ('300', *values[1:]) #('300', True, 'abracadabra', 100)
print(values)
values = values[:2] + ('changed',) + values[3:] #('300', True, '300', 100)
print(values)


