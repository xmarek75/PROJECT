new Vue({
    el: '#app',
    data: {
      file: null,
      message: null,
    },
    methods: {
      onFileChange(event) {
        this.file = event.target.files[0];
      },
      async uploadFile() {
        if (!this.file) {
          this.message = "No file selected";
          return;
        }
  
        const formData = new FormData();
        formData.append('file', this.file);
  
        try {
          const response = await fetch('http://localhost:5000/upload', {
            method: 'POST',
            body: formData,
          });
  
          const data = await response.json();
          this.message = data.message;
        } catch (error) {
          console.error('Error:', error);
          this.message = 'Failed to upload file';
        }
      },
    },
    template: `
      <div>
        <h1>Upload MP3 File for Transcription</h1>
        <form @submit.prevent="uploadFile">
          <input type="file" @change="onFileChange" />
          <button type="submit">Upload and Transcribe</button>
        </form>
        <div v-if="message">
          <p>{{ message }}</p>
        </div>
      </div>
    `,
  });
  