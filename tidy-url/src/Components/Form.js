import React from "react";
import axios from "axios";

const Form = ({ setHide, setUrl }) => {
	const handleSubmit = async (e) => {
		e.preventDefault();
		let url = e.target.url_input.value;
		let keyword = e.target.keyword_input.value;
		const fetchApi = `http://127.0.0.1:5000`;
		if (!url.includes("http://") && !url.includes("https://")) {
			url = "https://" + url;
		}

		try {
			let sendData = { original_url: url };
			if (keyword.length > 0) sendData.keyword = keyword;
			const { data } = await axios.post(fetchApi, sendData);
			if (data[0] === undefined) {
				setUrl(data.short_url);
			} else {
				setUrl(data[0].short_url);
			}
			setHide(true);
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
				required
			/>
			<label htmlFor="keyword_input">Keyword (Optional)</label>
			<input
				type="text"
				placeholder="Keyword..."
				name="keyword_input"
				id="keyword_input"
			/>
			<input type="submit" value="Shorten" className="submit_btn"></input>
		</form>
	);
};

export default Form;
