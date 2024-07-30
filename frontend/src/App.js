import React, { useState } from 'react';
import axios from 'axios';
import { PulseLoader } from 'react-spinners';

function App() {
    const [file, setFile] = useState(null);
    const [content, setContent] = useState('');
    const [summary, setSummary] = useState('');
    const [loading, setLoading] = useState(false);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleUpload = async () => {
        if (!file) {
            alert("Please select a file first.");
            return;
        }

        setLoading(true);
        try {
            const formData = new FormData();
            formData.append('file', file);
            const response = await axios.post('http://127.0.0.1:5000/upload', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            setContent(response.data.content);
            setSummary(response.data.summary);
        } catch (error) {
            console.error("Error uploading file:", error);
            alert("Error uploading file.");
        } finally {
            setLoading(false);
        }
    };

    const handleSummarize = async () => {
        if (!content) {
            alert("Please upload a file first or provide text.");
            return;
        }

        setLoading(true);
        try {
            const response = await axios.post('http://127.0.0.1:5000/summarize', { text: content });
            setSummary(response.data.summary);
        } catch (error) {
            console.error("Error summarizing text:", error);
            alert("Error summarizing text.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="App">
            <h1>Document Summarizer</h1>
            <input type="file" onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload</button>
            {loading ? (
                <div>
                    <PulseLoader color="#00BFFF" size={80} />
                    <p>Loading...</p>
                </div>
            ) : (
                <>
                    <h2>Content</h2>
                    <pre>{content}</pre>
                    <button onClick={handleSummarize}>Summarize</button>
                    <h2>Summary</h2>
                    <pre>{summary}</pre>
                </>
            )}
        </div>
    );
}

export default App;
