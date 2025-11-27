# Detector de Movimento com Python 📷

Este projeto utiliza a webcam para monitorar ambientes. Ao detectar movimento, o sistema emite um alerta sonoro (voz) e destaca a área da intrusão na tela.

## 🛠 Tecnologias Usadas
- Python 3
- OpenCV (Visão Computacional)
- Pyttsx3 / Spd-say (Sintetizador de Voz)

## ⚙️ Como Rodar

1.Clone o repositório:
``bash
git clone https://github.com/felipemaorrudo/detector-movimento-python.git
   
2.Crie um ambiente virtual:
No Linux/Mac:
python3 -m venv venv
source venv/bin/activate

No Windows:
python -m venv venv
venv\Scripts\activat

3.Instale dependências:
pip install -r requirements.txt

4.Execute o programa:
python movimento.py

(pressiona 'q' na janela da câmera para encerrar o programa)

Desenvolvido por Felipe Morrudo
