#------------------------------------------------------------------------#
# If you'd like you can launch the program from the command line using   #
# python danlog.py  [directory, filename]. However if you're not in the  #
# current path (C:/VssBOX/Generic Projects/DanLog/danlog.py) use         #
# C:/VssBOX/Generic Projects/DanLog/danlog.py in the command line        #
#------------------------------------------------------------------------#
from __future__ import with_statement
from __future__ import division
import sys, os, time

spath = r"C:\Users\q8knutk\Desktop\Crane"
all_result = []
assignment_list = {}
class bcolors:
   RED = '\033[30m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
   ENDC = '\033[0m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'

def start():
   if len(sys.argv) > 1:
      spath = r"C:\Users\q8knutk\Desktop\Crane"
      #os.chdir(spath)
      #root = os.getcwd().encode('string-escape')
      print("Still working")
      print(spath)
      pathname = os.path.join(spath, str(sys.argv[1]), str(sys.argv[2]))
      #path_to_file = os.path.abspath(pathname)
      print(pathname)
      if os.path.exists(pathname):
         print("Opening the file...")
         return search(pathname)
      else:
         print("File doesn't exists")
         raise ValueError
   #  for line in fileinput.input():
   #     path = os.path.abspath(line)
   #     #print os.path.abspath(pathname)
   #     getting_file(path)
   # except IOError:
   #  print(bcolors.OKBLUE + "That is not a valid directory or filepath, continuing with overview of all files ------->")
   else:
      print(bcolors.RED + "Giving you a overview of all the crane logs ------------->")
      search()
#print(sys.argv[0],len(sys.argv), sys.argv)

# input_user = raw_input("Do you want statistics over a certain crane file?")
# def handling_input():
#  if input_user == "no" or input_user == "NO" or input_user == '':
#     print( bcolors.FAIL + "We are giving you a overview of all the files")
#     search()
#
#  elif input_user == "yes" or input_user == "YES":
#     dict_name = raw_input("In which dictionary is the file located?")
#     file_name = raw_input("Please input filename:")
#     getting_file(file_name, dict_name)

def search(verb=''):
   global all_result
   queue = []
   result = {}
   count, fails, total_assignments = 0, 0, 0
   date = ''

   if verb == '':
      for (root, dirs, files) in os.walk(spath):
         for file in files:
            if file.endswith(".HSX"):
               print(os.path.join(root, file))
               queue.append(os.path.join(root, file))
               break
   else:
      queue.append(verb)

   if queue != []:
      for yas in queue:
         f = open(yas, "r")
         print(bcolors.OKBLUE + "Trying to open the first file in queue: %s" % yas )
         print(bcolors.FAIL + "Succesfully opened %s" % queue[0])
         print(bcolors.HEADER + "READING LINES ------------------------------------------------------------->")
         for line in f:
            count +=1
            if "CSR" in line:
               print(bcolors.ENDC + line)
               date = line[:14]
               crane_number = line[(line.index("CSR") + 3):(line.index("CSR") + 5)]
               if not crane_number in result:
                  result[crane_number] = 0
               if not line[-6:(len(line) - 3)] == '000':
                  fails += 1
                  result[crane_number] += 1
            elif "ACP" in line:
               print(bcolors.UNDERLINE + line)
               date = line[:14]
               crane_number = line[(line.index("ACP") + 3):(line.index("ACP") + 5)]
               if not crane_number in result:
                  result[crane_number] = 0
               if not line[-6:(len(line) - 3)] == '000':
                  fails += 1
                  result[crane_number] += 1
            elif "ARQ" in line:
               print(bcolors.ENDC + line)
               date = line[:14]
               crane_number = line[(line.index("ARQ") + 3):(line.index("ARQ") + 5)]
               if not crane_number in assignment_list:
                  assignment_list[crane_number] = 0
               else:
                  total_assignments += 1
                  assignment_list[crane_number] += 1
         f.close()
         if not date in all_result:
            all_result.append(date)
         else:
            pass
         all_result.append(result)
         result = {}
      for k, v in assignment_list.iteritems():
         print k, v
      print ("Amount of lines scanned:" + ' ' + str(count))
      print("Total crane fails:" + ' ' + str(fails))
      print("Total assignments given:" + ' ' + str(total_assignments))
      if fails > 0 and total_assignments > 0:
         percentage = fails / total_assignments
         print("Percentage of fail :" + ' ' + str(percentage) + '%')
      else:
         print("There were no assignments/fails")
      all_result = [x for x in all_result if x != {}]
      print(all_result)


   else:
      print('Nothin in queue')


if __name__ == "__main__":
   if len(sys.argv) >= 1:
      start()

   else:
      print("Something went wrong!")
      raise SystemError
