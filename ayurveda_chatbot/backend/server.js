const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const app = express();

app.use(cors()); // allow your frontend to access API
app.use(express.json());

// Connect to MongoDB Atlas
mongoose.connect('mongodb+srv://<username>:<password>@cluster0.abcde.mongodb.net/mydb?retryWrites=true&w=majority', {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => console.log('MongoDB Connected'))
.catch(err => console.error(err));

// Feedback Schema
const feedbackSchema = new mongoose.Schema({
    name: String,
    email: String,
    message: String,
    date: { type: Date, default: Date.now }
});
const Feedback = mongoose.model('Feedback', feedbackSchema);

// API endpoint to save feedback
app.post('/feedback', async (req, res) => {
    const { name, email, message } = req.body;
    try {
        const newFeedback = new Feedback({ name, email, message });
        await newFeedback.save();
        res.json({ success: true, msg: 'Feedback saved' });
    } catch (err) {
        res.status(500).json({ success: false, msg: 'Error saving feedback' });
    }
});

app.listen(5000, () => console.log('Server running on port 5000'));
