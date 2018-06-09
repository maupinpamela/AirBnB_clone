# AirBnB Clone
### Description
Holberton School's simple_shell ensures students grasp core concepts such including memory allocation and management, argc/argv, parent/child processes, and file i/o. Other basic concepts such as loops, arrays, structs, and pointers were employed in the making of this function.

### Environment
This function was developed and tested on `Ubuntu 14.04 LTS` via Vagrant in VirtualBox.

### File Contents
The repository contains the following files:

   **File**   |   **Description**
   -------------- | ---------------------
   AUTHORS | docker-formatted author file
   man_1_simple_shell | man page
   _itoa.c | functions to convert integer to an int
   args_execute.c | launches processes
   arg_to_path.c | searches for an argument in PATH env variable
   builtin_func.c | functions to handle built-in commands
   errors.c | functions to handle errors
   launch_prog.c | forks current process passes parsed input to execve
   parse_argv.c | splits string into an array of single word tokens
   read_line.c | uses getline to read input from STDIN
   README.md | readme file
   shell_loop.c | controls flow of the shell
   simple_shell.c | entry point that imports env and invokes shell_loop
   simple_shell.h | header file
   strutil.c | five replica standard library utility string functions
   util.c | misc utility functions; mostly standard library replicas

### Function Descriptions

 **Function** | **Description**
 -------------- | -----------------
 int main(int argc, char **argv, char **env) | entry point
 int count_digit(int n) | count the number of digits in an int
 char *_itoa(int n) | converts an integer to ASCII character
 int args_execute(char **m_argv, char **args, char **env) |  launches built-in commands
 int launch_prog(char **m_argv, char **args, char **env) | forks current process passes parsed input to execve
 char **parse_argv(char *line) | splits string into an array of single word tokens
 line_t read_line(void) | uses getline to read input from STDIN
 void shell_loop(char **m_argv, char **env) | controls flow on the shell
 int ss_env(char *args, char **env) | prints the environment
 int ss_exit(char *args, char **env) | exits the shell
 void ss_ctrlc(int signum) | prevents ctrl-c from exiting the shell
 char *arg_to_path(char **argv, char **env) | searches for an argument in PATH env variable
 char *env_find(const char *name, int *offset, char **env) | searches environment list for name
 char *_memcpy(char *dest, char *src, unsigned int n) | copies memory area
 void *_realloc(void *ptr, size_t size) | changes size of memory block
 int _strncmp(const char *s1, const char *s2, size_t n) | compares first n bytes of s1 to s2
 int _strlen(char *s) | calculates the length of a string
 char *_strdup(char *s) | duplicates a string
 char *_strncpy(char *destn, const char *src, size_t n) | copies a string
 char *_strncat(char *destn, const char *src, size_t n) | concatenates two strings
 char *_getenv(const char *name, char **env) | searches envirnment list for name
 int _strcmp(char *s1, char *s2) | compares two strings
 int no_args(char **argv) | error when req'd arg(s) are not given
 void fork_error(cahr **argv) | error when fork fails
 void execve_error(char **argv) | error when execve fails
 int null_arg_w_free(char *converted_arg, char **argv, char *s, int err_cnt) | error when malloc in arg_to_path fails
 void execve_error_w_free(char *converted_arg, char **argv) | error when execve fails that frees memory

### Usage and Installation
Clone the repository and then compile using gcc.
```
$ git clone https://github.com/AfaMadza/simple_shell
```
### Compilation

This code was compiled with the following flags:
` gcc -Wall -Werror -Wextra -pedantic *.c -o hsh `

###### Example command line call (non-interactive mode)

```

$ echo "/bin/ls" | ./hsh
README.md       builtin_func.c  read_line.c    simple_shell.h  util.c
arg_to_path.c   launch_prog.c  shell_loop.c    strutil.c       args_execute.c
hsh             parse_argv.c   simple_shell.c
$

```

###  Roadmap

---

### Authors

* [**Afa Madza**](https://github.com/AfaMadza)
* [**Pamela Maupin**](https://github.com/maupinpamela)

<p align="center">
<a href="https://www.holbertonschool.com"><img src="https://intranet.hbtn.io/assets/holberton-logo-simplified-d4e8a1e8bf5ad93c8c3ce32895b4b53749b477b7ba7342d7f064e6883bcd3be2.png"></a>
</p>