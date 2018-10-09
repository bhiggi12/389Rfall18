section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        ;your code goes here!
                                      ; memset(char *str, char val, int strl)
        mov     QWORD [rbp-24], rdi   ; 1st parameter in rdi
        mov     eax, esi              ; 2nd parameter in esi
        mov     DWORD  [rbp-32], edx  ; 3rd parameter in rdx
        mov     BYTE  [rbp-28], al    ; store 2nd parameter in stack (byte)
        mov     DWORD  [rbp-4], 0     ; local variable i = 0
        jmp     memset_loop           ; go to loop conditions

memset_loop_body:                     ; str[i] = val;
        mov     eax, DWORD [rbp-4]    ; move local variable into the temporary register
        cdqe                          ; Convert dword (eax) to qword (rax)
        add     rax, QWORD [rbp-24]   ; add the value to the 1st parameter
        movzx   edx, BYTE  [rbp-28]   ;
        mov     BYTE  [rax], dl       ; because dl is a lower level, need to use BYTE to put in 64 bit register
        add     DWORD  [rbp-4], 1     ; add 1 to the local variable

memset_loop:                          ; for (i=0; i < strl; i++)
        mov     eax, DWORD  [rbp-4]   ; store the value of i in temporary register
        cmp     eax, DWORD  [rbp-32]  ; compare i to strl
        jl      memset_loop_body      ; jump if i < strl

        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!


global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame


        ;;;;;;;;;;;;;;;;;;;;;
        ;your code goes here!
        ;;;;;;;;;;;;;;;;;;;;;

                                       ; void memset(char *dst, char *src, int len)
        mov     QWORD [rbp-24], rdi    ; 1st parameter in rdi
        mov     QWORD [rbp-32], rsi    ; 2nd parameter in rsi
        mov     DWORD [rbp-36], edx    ; 3rd parameter in edx
        mov     DWORD [rbp-4], 0       ; local variable int i, initiate to 0
        jmp     strncpy_loop           ; for loop conditions

strncpy_loop_body:                     ; dst[i] = src[i]
       mov     eax, DWORD [rbp-4]      ; load the value of i into temporary register
       movsxd  rdx, eax                ; move the value of i into rdx
       mov     rax, QWORD [rbp-32]     ; load the value of 2nd parameter into temporary register
       add     rax, rdx                ; move the
       mov     edx, DWORD[rbp-4]       ;
       movsxd  rcx, edx                ;
       mov     rdx, QWORD [rbp-24]     ;
       add     rdx, rcx                ;
       movzx   eax, BYTE [rax]         ;
       mov     BYTE[rdx], al           ; move the one byte to 64 bit register
       add     DWORD  [rbp-4], 1       ;

strncpy_loop:                          ; for (i = 0; i < len; i++)
        mov     eax, DWORD  [rbp-4]    ; store the value of i in temporary register
        cmp     eax, DWORD  [rbp-36]   ; compare the value of i to the 3rd parameter
        jl      strncpy_loop_body      ; jump to the loop body if the above computation is less than

        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!
