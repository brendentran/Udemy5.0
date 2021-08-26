oice = "-"
computer_parts = [] # create an empty list

while current_choice != '0':
        if current_choice in "12345":
                    print("Adding {}".format(current_choice))
                            if current_choice == '1':
                            computer_parts.append("comuter")
                            elif current_choice == '2':
                                                                    computer_parts.append("monitor")
                                                                            elif current_choice == '3':
                                                                                            computer_parts.append("keyboard")
                                                                                                    elif current_choice == '4':
                                                                                                                    computer_parts.append("mouse")
                                                                                                                            elif current_choice == '5':
                                                                                                                                            computer_parts.append("mouse pad")

                                                                                                                                                else:
                                                                                                                                                            print("Please add options from the list below:")
                                                                                                                                                                    print("1: computer")
                                                                                                                                                                            print("2: monitor")
                                                                                                                                                                                    print("3: keyboard")
                                                                                                                                                                                            print("4: mouse")
                                                                                                                                                                                                    print("5: mouse pad")
                                                                                                                                                                                                            print("0: to finish")

                                                                                                                                                                                                                current_choice = input()

                                                                                                                                                                                                                print(computer_parts)
