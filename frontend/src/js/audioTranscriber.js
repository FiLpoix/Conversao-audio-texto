document.getElementById('audioForm').addEventListener('submit', async (event) => {
    event.preventDefault(); // Evita o recarregamento da página

    const apiUrl = 'http://127.0.0.1:8000/api/transcribe/';
    const formData = new FormData();
    const audioFile = document.getElementById('audioFile').files[0];

    if (!audioFile) {
        alert('Por favor, selecione um arquivo de áudio.');
        return;
    }

    formData.append('audio', audioFile);

    try {
        // Enviar solicitação ao web service
        const response = await fetch(apiUrl, {
            method: 'POST',
            body: formData,
        });
        
        
        // Verificar se a resposta foi bem-sucedida
        if (!response.ok) {
            throw new Error(`Erro na transcrição: ${response.status}`);
        }

        const data = await response.json();
        
        // Exibir a transcrição no elemento de saída
        document.getElementById('output').textContent = data.transcription;
    } catch (error) {
        console.error('Erro ao enviar a solicitação:', error);
        document.getElementById('output').textContent = `Erro: ${error.message}`;
    }
});
