#include <string>
#include <iostream>
#include <sstream> //for string stream operations
#include <vector> //for dynamic array operations
#include <stdlib.h>  //for exit function
#include <wait.h> //for waitpid function
#include <unistd.h> //for fork and execvp functions
#include <cstring> //for strerror function
#include <errno.h> //for error handling

using namespace std;

/*parse_args: takes a string line and a reference to a vector
of strings cmds. It splits the input string into individual
tokens (commands) using spaces as delimiters and stores them
in the cmds vector.*/
void parse_args(string line, vector<string> &cmds){
    stringstream liness(line);
 
    string token;
    while (getline(liness, token, ' ')) {
        cmds.push_back(token);
    }
}

/*print_history: takes a constant reference to a vector of
strings history. It prints the command history, with each
command numbered starting from 1*/
void print_history(const vector<string> &history) 
{
    int count = 1;
    for (const string &cmd : history) //"for each const string object cmd in the history vector"
    //history: This is the range expression, which specifies the container to iterate over.
    { 
        cout << count << ". " << cmd << endl;
        count++;
    }
}

int main(void)
{
    vector<string> history;
    int interrupt_count = 0;
    
    while (1)
    {
        // prompt user for input
        cout << "New Shell (guish).&nbsp ";

        string cmd;
        getline(cin, cmd);

        // ignore empty input
        if (cmd == "" || cmd.size() == 0) 
            continue;

        //Prints the received user command
        cout <<"Received user commands: ";
        cout << cmd << endl;
        
        // built-in: exit
        if (cmd == "help")
        {
            cout << "help\n";
            continue;
        }
        else if(cmd == "exit")
        {
            exit(0);
        }

        // built-in: hist
        else if (cmd == "hist") 
        {
            print_history(history);
            continue;
        }
// built-in: r n
/*The code checks if the input command cmd meets the following conditions:

cmd.size() > 2: The command string must have more than 2 characters.
cmd[0] == 'r': The first character of the command string must be 'r'.
cmd[1] == ' ': The second character of the command string must be a space.*/
        else if (cmd.size() > 2 && cmd[0] == 'r' && cmd[1] == ' ') 
        {
            int n = stoi(cmd.substr(2)); //stoi converts string to integer").
            /*stoi(Extract) substring from command starting index 2 to the end.
            This is because the first two characters are 'r' 
            and a space, and we want to extract the remaining part of the string.*/

            if (n >= 1 && n <= history.size()) //checks if the extracted history index n is valid
            {
                cout << "Executing command from history: " << history[n - 1] << endl;
                cmd = history[n - 1];
            } else {
                cout << "Invalid history index." << endl;
                continue;
            }
        }

        vector<string> cmd_args;
        parse_args(cmd, cmd_args);

        // Add command to history
        history.push_back(cmd);
        if (history.size() > 10) {
            history.erase(history.begin());
        }

        // fork child and execute program
        int pid = fork();
        int status;
        if (pid == 0)
        {
            /*Creates an array of C-style strings (char**) from the cmd_args vector.
            Executes the command using execvp. If execvp returns, prints an error message and exits.*/
            char **argv = new char*[cmd_args.size() + 1];
            for (size_t i = 0; i < cmd_args.size(); ++i) {
                argv[i] = const_cast<char*>(cmd_args[i].c_str());
            }
            argv[cmd_args.size()] = NULL;
            
            execvp(argv[0], argv);
            // If execvp returns, there was an error
            cerr << "Error executing command: " << strerror(errno) << endl;
            delete[] argv;
            exit(1);
        }
        else
        {/*In the parent process:
           Waits for the child process to finish using waitpid.
             Prints the exit status of the child process if it exited abnormally.*/
            // wait for program to finish and print exit status
            waitpid(pid, &status, 0);
            if (WIFEXITED(status) && WEXITSTATUS(status) != 0) {
                cout << "program returned exit code: " << WEXITSTATUS(status) << endl;
            }
        }
    }
}
/*Overall, this code provides a basic shell that can execute user commands, manage a
command history, and handle built-in commands.*/
