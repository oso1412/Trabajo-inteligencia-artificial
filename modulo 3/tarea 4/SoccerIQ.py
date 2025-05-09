print('====BIENVENIDO A SOCCERIQ EL SISTEMA EXPERTO QUE TE RESOLVERA LAS DUDAS DE QUE TIPO DE ACCION SE HARA EN UN PARTIDO DE FUTBOL====')  
print('NOTA: Responde todas las preguntas con si o no TODO EN MINUSCULAS')  

salio_balon=input('El balon salio de la cancha?')
if(salio_balon == 'si'):
    por_la_vertical=input('Salio por la vertical?')
    if(por_la_vertical == 'si'):
        toque_del_equipo=input('Fue toque del equipo defensor?')
        if(toque_del_equipo=='si'):
            print('Es tiro de esquina')
        else:
            print('Saque de meta')
    else:
       print('Es saque de banda')    
else:
    fue_falta=input('La accion fue una falta?')
    if(fue_falta == 'si'):
        dentro_del_area=input("La falta fue dentro del area?")
        if(dentro_del_area == 'si'):
            en_ataque=input("La falta en ataque?")
            if(en_ataque == 'si'):
                print('Tiro libre a favor')    
            else:
                print('Penalti')        
        else:
            print('Tiro libre en contra')    
            
    else:
        fuera_juego=input('Fue fuera de lugar?')
        if(fuera_juego=='si'):
            print('Balon parado')
        else:
            lesionado=input('Hay un jugador lesionado?')
            if(lesionado=='si'):
                print('Bote a tierra')
            else:
                cambio=input('Hubo cambio?')
                if(cambio=='si'):
                    print('Entra jugador')
                else:
                    acabo_tiempo=input('Se acabo el tiempo?')
                    if(acabo_tiempo=='si'):
                        minuto45=input('Los primeros 45 minutos?')
                        if(minuto45=='si'):
                            compensacion=input('Se añadio tiempo de compensacion?')
                            if(compensacion=='si'):
                                acabo_compensacion=input('Se acabo el tiempo de compensacion?')
                                if(acabo_compensacion=='si'):
                                    print('Se va al descanso')
                                else:
                                    print('Sigue el juego')
                            else:
                                print('Se acabo el primer tiempo')
                        else:
                            compensacion2=input('Se añadio tiempo de compensacion?')
                            if(compensacion2=='si'):
                                acabo_compensacion2=input('Se acabo el tiempo de compensacion?')
                                if(acabo_compensacion2=='si'):
                                    print('Se acabo el partido')
                                else:
                                    print('Sigue el juego')
                            else:
                                acabo_tiempo2=input('Se acabo el tiempo reglamentario?')
                                if(acabo_tiempo2=='si'):
                                    eliminatoria=input('Es eliminatoria?')
                                    if(eliminatoria=='si'):
                                        empate=input('Acabo en empate?')
                                        if(empate=='si'):
                                            tiempo_extra=input('Se agrego tiempo extra?')
                                            if(tiempo_extra=='si'):
                                                acabo_TE=input('Se acabo el tiempo extra?')
                                                if(acabo_TE=='si'):
                                                    gano=input('Gano un equipo?')
                                                    if(gano=='si'):
                                                        print('El equipo ganador pasa a la siguiente ronda del torneo')
                                                    else:
                                                        print('Se va a penales')
                                                else:
                                                    print('Sigue el partido')
                                            else:
                                                print('Se acabo el partido')
                                        else:
                                            print('El equipo peerdedor quedo eliminado del torneo')
                                    else:
                                        fase_de_grupos=input('Es fase de grupo?')
                                        if(fase_de_grupos=='si'):
                                            es_empate=input('El partido es empate?')
                                            if(es_empate=='si'):
                                                print('Un punto para cada equipo')
                                            else: 
                                                print('Tres puntos para el ganador')
                                        else:  
                                            es_liga=input('Es partido dee liga?')
                                            if(es_liga=='si'): 
                                                es_empate=input('El partido es empate?')
                                                if(es_empate=='si'):
                                                    print('Un punto para cada equipo')
                                                else: 
                                                    print('Tres puntos para el ganador') 
                                            else:
                                                  print('El partido es un partido amistoso')        
                    else:
                        balon_porteria=input('Se metio el balon a la porteria?')
                        if(balon_porteria=='si'):
                            mismo_equipo=input('El balon lo metio un jugador del mismo equipo')
                            if(mismo_equipo=='si'):
                                print('Autogol')
                            else:
                                print('Gol')
                        else:
                            publico=input('Se metio el publico?')
                            if(publico=='si'):
                                print('Se para el juego')
                            else:
                                balon2=input('Hay 2 balones en el juego?')
                                if(balon2=='si'):
                                    print('Se saca el segundo balon')
                                else:
                                    print('No se para el partido')