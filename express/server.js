const express = require ('express')
const axios = require('axios')
const cors = require('cors')
require('dotenv').config()

const app = express()

app.use(express.json())
app.use(cors())

const FASTAPI_URL = "http://127.0.0.1:8000/recommend-outfit";


app.post('/get-outfit', async(req,res)=>
{
    try{
        const temperature = req.body.temperature
        const humidity = req.body.humidity
        const weather_condition = req.body.weather_condition

        const response = await axios.post(FASTAPI_URL,
            {
                temperature,
                humidity,
                weather_condition
            }
            
        )
        res.json(response.data);
        
    }
    catch(error)
    {
        console.error("Error:", error);
        res.status(500).json({ error: "Error connecting to FastAPI" })

    }
    
    
})

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Express.js server running on port ${PORT}`));