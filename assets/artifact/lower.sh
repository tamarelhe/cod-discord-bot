#!/bin/bash

# Loop através dos arquivos na pasta
for arquivo in *
do
  # Verifique se o arquivo existe e se é um arquivo
  if [ -f "$arquivo" ]; then
    # Converta o nome do arquivo para letras minúsculas
    novo_nome=$(echo "$arquivo" | tr '[:upper:]' '[:lower:]')
    
    # Renomeie o arquivo
    mv "$arquivo" "$novo_nome"
  fi
done

for file in *
do
  if [[ $file == *-* ]]; then
    mv "$file" "${file//-/_}"
  fi
done