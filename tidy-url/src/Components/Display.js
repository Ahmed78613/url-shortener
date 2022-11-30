import React from "react";

const Display = ({ url }) => {
	const copyToClipboard = () => {
		const shortUrl = document.getElementById("short_url");
		console.log(shortUrl.textContent);
		navigator.clipboard.writeText(url);
	};

	return (
		<div className="container">
			<h2>Heres your Tidy Url!</h2>
			<a href={url} id="short_url">
				{url}
			</a>
			<i
				onClick={copyToClipboard}
				id="copy_btn"
				class="fa-regular fa-clipboard"
			></i>
		</div>
	);
};

export default Display;
