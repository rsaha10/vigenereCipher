#vigenere cipher

run:
	python vig.py

	make encode ARGS="plaintext key True"

	make decode ARGS="plaintext key False"
