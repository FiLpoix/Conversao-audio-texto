document.getElementById('generateButton').addEventListener('click', async(event)=> {
    event.preventDefault()

    const text = document.getElementById('textInput').value;
    
    if (text.trim() === '') {
        alert('Por favor, insira um texto.');
        return;
    }
    const formData = new FormData();
    formData.append('text', text);

    // Enviar o texto para a API do Django
    try{
    const response = await fetch(`http://127.0.0.1:8001/api/text-to-audio/`, {
        method: 'POST',
        body: formData,
    })
            
        // Verificar se a resposta foi bem-sucedida
        if (!response.ok) {
            throw new Error(`Erro na transcrição: ${response.status}`);
        }

        const data = await response.json();
        
        const audioPlayer = document.getElementById('audioPlayer');
                audioPlayer.src = `../backend/text_to_audio${data.file_url}`;
                // ..\backend\text_to_audio
                console.log(data)
                audioPlayer.play();
    } catch (error) {
        alert('Erro ao gerar o áudio: ' + error);
    }
        
});