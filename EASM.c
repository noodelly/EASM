#include <stdio.h>
#include <string.h>

void optimize()
{
    //Load external optimize
}

void gen()
{

}

void semantic()
{

}

void syntax()
{

}

void lexer(char line[])
{
    int pointer;
    for(pointer = 0; pointer < sizeof(line); pointer++)
    {
        //Remove whitespace
        if(line[pointer] == " " || line[pointer] == "   ")
        {
            line[pointer] = "";
        }

       
    }

     printf("%s", line);
     
}

int main(int argc, char *argv[])
{
    FILE *source;
    int read, ret, i;
    source = fopen(argv[1], "r");
    printf("EASM Assembler (indev)\n");
    printf("Target source is %s:\n", argv[1]);

    if(source != NULL){
        i = 0;
        while(1)
        {
            if(feof(source)) break;

            char line[255];
            
            fgets(line, sizeof(line), source);
            lexer(line);
           // printf("%d: %s", i, line);
            
            
            i++;
        }
        
        if(ret != 0) { optimize(); }   //Check for '-no' flag
        gen();

        printf("Target: %s assembled successfully!\n", argv[1]);

        fclose(source);

    } else {printf("Target source '%s' could not be found.", argv[1]);}

    return 0;
}