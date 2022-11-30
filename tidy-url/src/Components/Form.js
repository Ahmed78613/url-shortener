import React from "react";
import axios from "axios";

const Form = ({ setHide, setUrl }) => {
	const handleSubmit = async (e) => {
		e.preventDefault();
		let url = e.target.url_input.value;
		console.log(url);
		const fetchApi = `http://127.0.0.1:5000`;
		if (!url.includes("http://www.") || !url.includes("https://www.")) {
			url = "http://www." + url;
		}
		try {
			const { data } = await axios.post(fetchApi, { original_url: url });
			setHide(true);
			setUrl(data.short_url);
		} catch (err) {
			console.error(err);
		}
	};

	return (
		<form onSubmit={handleSubmit} className="container">
			<label htmlFor="">Long url</label>
			<input
				type="text"
				placeholder="Enter long url..."
				name="url_input"
				id="url_input"
			/>
			<input type="submit" value="Shorten" className="submit_btn"></input>
		</form>
	);
};

export default Form;
