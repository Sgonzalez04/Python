
numing=int(input("ingrese el numero de estudiantes ingles"))
suscritosingles=set(input("digite ids estudiantes ingles").split( ))
#split me manda una lista con espacios
#set permire almacenar varios elementos en una lista

numfran=int(input("ingrese el numero de estudiantes frances"))
suscritosfran=set(input("ingrese el ids de estudiantes frances".split()))

solo_ingles=suscritosingles-suscritosfran
print(len(solo_ingles))
#len cantidad elementos en una lista