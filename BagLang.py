
print ("Newcomer greeting")

public class Freshy66 
{ 
    public static void main (Str ing [ ] args) 
        { 
            System.out. println("Fresh arrival"); 
        } 
}


#include <stdio.h> 
int main  ( )
{ 
    printf("Freshy reception \n"); 
    return 0; 
}


console.log ("Welcome newbie");

puts "Welcome  to  IT Department FITM@KMUTNB"

package main

import "fmt"

func main() {
    fmt.Println("Hello 66")
}

fn main() {
    println!("We are welcome");
}


<!DOCTYPE html>
<html>
<head>
    <title>Welcome Message</title>
</head>
<body>
    <p>All are welcome</p>
</body>
</html>


section .data
    message db 'Good day boys and girls', 0

section .text
    global _start

_start:
    ; Print the message
    mov eax, 4         ; System call number for write
    mov ebx, 1         ; File descriptor for stdout
    mov ecx, message   ; Address of the message
    mov edx, 23        ; Length of the message
    int 0x80           ; Call the kernel

    ; Exit the program
    mov eax, 1         ; System call number for exit
    xor ebx, ebx       ; Exit status 0
    int 0x80           ; Call the kernel

<?php
echo "Good day boys and girls";
?>