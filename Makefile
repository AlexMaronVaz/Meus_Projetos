compilar:
	gcc -c arquivo.c -o arquivo.o
criar_executavel:
	gcc arquivo.o -o arquivo
executar:
	./arquivo

criar_arquivos:
	touch 1.jpg 2.pdf 3.mp4
criar_pastas:
	mkdir Imagens Documentos Vídeos
organizar_arquivos:
	mv *.jpg Imagens
	mv *.pdf *.c *.o Documentos
	mv *.mp4 Vídeos

python:
	python3 -c "x = int(input('Digite um valor para x: ')); y = int(input('Digite um valor para y: ')); z = x + y; print('A soma entre x e y é',z)"
