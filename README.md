# Avaliação Técnica — Python (Fibonacci recursivo)

🖥️ Tema: Python

📌 Tarefa: Escrever um script que recebe como parâmetro um número inteiro positivo n e imprime o n-ésimo valor da sequência de Fibonacci usando recursão.

🧭 Convenção adotada: F(1)=0, F(2)=1 (logo, para n=9 o resultado é 34).

📖 Enunciado (resumo):

Dado um n inteiro positivo, imprimir no console o n-ésimo termo da sequência de Fibonacci.
Exemplo: Entrada: 9 → Saída esperada: 34.

📖 Arquivo
fibonacci.py — implementação recursiva com otimização via cache.

Como executar: 

🎮 Opção A — Localmente (recomendado)

Instale o Python 3.

No terminal, dentro da pasta do projeto, rode:

- Windows: python fibonacci.py 9
  
- macOS / Linux: python3 fibonacci.py 9

✅ Saída esperada: 34

🎮 Opção B — OnlineGDB (execução no navegador)

1- Abra o site: https://www.onlinegdb.com - (ambiente online para executar/depurar Python).

2- Apague o código padrão e cole o conteúdo de fibonacci.py.

3- Clique em Run para executar.

📖 Sobre a otimização (lru_cache): 
Para eliminar recomputações na recursão, foi usado o decorator lru_cache do módulo functools.
Ele memoriza resultados de chamadas anteriores, acelerando muito para valores maiores de n, mantendo a solução recursiva conforme o enunciado.

✅ Validações: 
Aceita apenas inteiros positivos (mostra mensagem de erro caso contrário).
Exemplo de teste interno:
assert fib_cache(9) == 34

⚠️ Observações:
O script usa a convenção F(1)=0, F(2)=1. Se você usar F(0)=0, F(1)=1, o índice muda e n=9 retorna 21, não 34.

## Autores
- [Purgano](https://github.com/Purgano)

