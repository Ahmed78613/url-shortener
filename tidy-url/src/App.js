import "./index.css";
import React, { useState } from "react";
import Form from "./Components/Form";
import Display from "./Components/Display";

function App() {
	const [hide, setHide] = useState(false);
	const [url, setUrl] = useState("");

	const reset = () => {
		setHide(false);
		setUrl("");
	};

	return (
		<div className="App">
			<h1 onClick={reset}>Tidy Url</h1>
			{!hide ? (
				<Form setHide={setHide} setUrl={setUrl} />
			) : (
				<Display url={url} />
			)}
		</div>
	);
}

export default App;
