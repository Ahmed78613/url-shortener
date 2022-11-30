import React from 'react'
import axios from 'axios'

const Form = ( {setHide, setUrl} ) => {
    const handleSubmit = async (e) => {
        e.preventDefault()
        let url = e.target.url_input.value
        console.log(url)
        const fetchApi = `http://127.0.0.1:5000`
        if (!url.includes('http://www.' )  || !url.includes('https://www.' )) {
            url = 'http://www.' + url
        }
        try {
            const {data} = await axios.post(fetchApi, {'original_url':url});
            console.log('*****************')
            console.log(data)
            console.log('*****************')
            setHide(true)
            setUrl(data.short_url)
        } catch (err) { 
            console.error(err)
            console.log("FAIL FAIL");
        }
    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label>
                    Enter URL to be shortened
                    <input type="text" placeholder="URL" name="url_input" id="url_input"></input>
                </label>
                <input type="submit" value="Shorten" className="submit_btn"></input>
            </form>
        </div>
    )
}

export default Form
