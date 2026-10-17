import colorama
import time
import random
import sys
from colorama import Fore, Back
time_start = time.time()
topic = "KD text lab v6.0.0"
file = "filecreatedfromKD_text_lab_v6.0.0.txt"
print(f"you are using {Fore.GREEN + topic + Fore.RESET} on {Fore.MAGENTA + sys.platform + Fore.RESET} platform ")
name = input(Fore.CYAN + "enter your name to continue: " + Fore.RESET)
print(Fore.YELLOW + f"hello {Fore.CYAN + name + Fore.RESET}!" + Fore.RESET)
print("what you want to do?")
while True:
  print(Fore.MAGENTA + "1. edit text" + Fore.RESET)
  time.sleep(0.1)
  print(Fore.RED + Back.YELLOW + "2. EXIT" + Fore.RESET + Back.RESET)
  try:
    ques1 = int(input("enter only in number: "))
    if ques1 == 2:
      print(Fore.GREEN + "exiting..." + Fore.RESET)
      time.sleep(0.3)
      print(Fore.GREEN + "exited sucessfully" + Fore.RESET)
      break
    elif ques1 == 1:
      print(Fore.YELLOW + "loading sys..." + Fore.RESET)
      time.sleep(0.78)
      print(Fore.BLUE + "sys loaded successfully" + Fore.RESET)
      with open(file, "a+") as file_1:
        input_data = input(Fore.RED + "what do you want to write?: " + Fore.RESET)
        file_1.write(input_data + "\n")
      while True:
        print(Fore.RED + "1. count text(words)" + Fore.RESET)
        time.sleep(0.1)
        
        print(Fore.MAGENTA + "2. capital all text" + Fore.RESET)
        time.sleep(0.1)
        print(Fore.BLUE + "3. uncapital all text" + Fore.RESET)
        time.sleep(0.1)
        print(Fore.YELLOW + "4. reverse text" + Fore.RESET)
        time.sleep(0.1)
        print(Fore.GREEN + "5. count alphabet(including space)" + Fore.RESET)
        time.sleep(0.1)
        print(Fore.RED + "6. test the sentence if it contains only alphabets:" + Fore.RESET)

        time.sleep(0.1)
        print(Fore.MAGENTA + "7. test the sentence if it contains any number:" + Fore.RESET)
        time.sleep(0.1)
        print(Fore.CYAN + "8. split test" + Fore.RESET)
        time.sleep(0.1)
        print(Fore.RED + "9. swap case it will convert capital to small and small to capital" + Fore.RESET)
        time.sleep(0.1)
        print(Fore.MAGENTA + "10. title it will captial the first letter of sentence")
        time.sleep(0.1)
        print(Fore.GREEN + "11. captilize it will capital  first letter of sentence" + Fore.RESET)
        time.sleep(0.1)
        print(Fore.BLUE + "12. Find a alphabet or number it will find alphabet and number symobol etc. " + Fore.RESET)
        time.sleep(0.1)
        print(Fore.WHITE + "13. time used this app? " + Fore.RESET)
        time.sleep(0.1)
        print(Fore.RED + Back.YELLOW + "14. Exit" + Fore.RESET + Back.RESET)
        time.sleep(0.1)
        try:
          enter_choice = int(input("enter only in number: "))
          match enter_choice:
            case 14:
              print(Fore.YELLOW + "exiting..." + Fore.RESET)
              time.sleep(0.3)
              print(Fore.GREEN + "exited successfully")
              exit()
            case 1:
              with open(file, "r") as file_1:
                lines = file_1.read()
                if not lines:
                  print("empty data")
                else:
                  
                  print(Fore.MAGENTA + f"you wrote {len(lines.split())} words")
                  file_1.seek(0)
            case 2:
              with open(file, mode="r") as file_1:
                data: Unknown = file_1.read()
                if not data.strip():
                  print(Fore.YELLOW + "empty data" + Fore.RESET)
                else:
                  capital_input_data = data.upper()
                  print(capital_input_data)
                  with open(file, "w") as file_1:
                    file_1.write(capital_input_data)
            case 3:
              with open(file, "r") as file_1:
                data = file_1.read()
                if not data.strip():
                  print(Fore.YELLOW + "empty data")
                else:
                  uncapital_input_data = data.lower()
                  with open(file, "w") as file_1:
                    file_1.write(uncapital_input_data)
                  print(uncapital_input_data)
            case 4:
              with open(file, "r") as file_1:
                data = file_1.read()
              if not data:
                print(Fore.YELLOW + "empty data" + Fore.RESET)
              else:
                with open(file, "r") as file_1:
                  
                 data = file_1.read()
                if not data:
                  print(Fore.YELLOW + "empty data" + Fore.RESET)
                else:
                  reverse_input_data = data[::-1]
                  print(reverse_input_data)
                  with open(file, "w+") as file_1:
                    file_1.write(reverse_input_data)
            case 5:
              with open(file, "r") as file_1:
                data = file_1.read()
                if not data:
                  print(Fore.YELLOW + "empty data" + Fore.RESET)
                else:
                  with open(file, "r") as file_1:
                    file_1.seek(0)
                    print(len(data))
            case 6:
              with open(file, "r") as file_1:
                file_1.seek(0)
                data = file_1.read()
                data.strip()
                if not data:
                  print(Fore.YELLOW + "empty data" + Fore.RESET)
                else:
                  with open(file, "r") as file_1:
                    is_aplha = data.isalpha()
                    if is_aplha == True:
                      print(Fore.GREEN +  "it contains only alphabets" + Fore.RESET)
                    elif is_aplha == False:
                      print(Fore.RED + "not contains alphabets" + Fore.RESET)
                    else:
                      print(Fore.RED + Back.YELLOW + "aborted" + Fore.RESET+Back.RESET)
            case 7:
              with open(file, "r") as file_1:
                file_1.seek(0)
                data = file_1.read()
                data.strip()
                if not data:
                  print(Fore.YELLOW + "empty data" + Fore.RESET)
                else:
                  with open(file, "r") as file_1:
                    is_num = data.isdigit()
                    if is_num == True:
                      print(Fore.GREEN +  "it contains only numbers" + Fore.RESET)
                    elif is_aplha == False:
                      print(Fore.RED + "not contains numbers" + Fore.RESET)
                    else:
                      print(Fore.RED + Back.YELLOW + "aborted" + Fore.RESET+Back.RESET)
            case 8:
              with open(file, "r" ) as file_1:
                data = file_1.read()
                if not data:
                  print(Fore.YELLOW + "empty data" + Fore.RESET)
                else:
                  with open(file, "w+") as file_1:
                    list_input_data = list(data)
                    split_input_data = data.split()
                    print(split_input_data)
                    str_input_data = str(split_input_data)
                    file_1.write(str_input_data)
            case 9:
              with open(file, "r") as file_1:
                data = file_1.read()
                if not data:
                  print(Fore.YELLOW + "empty data" + Fore.RESET)
                else:
                  with open(file, "w+") as file_1:
                    swap_case_input_data = data.swapcase()
                    print(swap_case_input_data)
                    file_1.write(swap_case_input_data)
            case 10:
              with open(file, "r") as file_1:
                data = file_1.read()
                if not data:
                  print(Fore.YELLOW + "empty data" + Fore.RESET)
                else:
                  with open(file, "w+") as file_1:
                    title_input_data = data.title()
                    print(title_input_data)
                    file_1.write(title_input_data)
            case 11:
              with open(file, "r") as file_1:
                data = file_1.read()
                if not data:
                  print(Fore.YELLOW + "empty data" + Fore.RESET)
                else:
                  with open(file, "w+") as file_1:
                    captilize_input_data = data.capitalize()
                    print(captilize_input_data)
                    file_1.write(captilize_input_data)
            case 12:
              with open(file, "r") as file_1:
                data = file_1.read()
                if not data:
                  print(Fore.YELLOW + "empty data" + Fore.RESET)
                else:
                  with open(file, "r") as file_1:
                    search_input_data_input_value = input(Fore.GREEN + f"enter text to find in {Fore.MAGENTA + data + Fore.RESET} if text exists in data: " + Fore.RESET)
                    search_input_data = data.find(search_input_data_input_value)
                    if search_input_data >= 0:
                      print(Fore.GREEN + f"text founded✓\nin {search_input_data} index" + Fore.RESET)
                    elif search_input_data == -1:
                      print(Fore.RED + "text not founded" + Fore.RESET)
            case 13:
              time_stop = time.time()
              total_time_taken = time_stop-time_start
              print(Fore.CYAN + f" {str(round(total_time_taken)) + Fore.RESET} seconds")
        except ValueError:
          print(Fore.RED + 'invalid input' + Fore.RESET)
  except ValueError:
    print(Fore.RED + "invalid input" + Fore.RESET)
