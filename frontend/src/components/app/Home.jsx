import { useEffect } from "react";
import { useNavigate } from "react-router";

const Home =()=>{
	const navigate = useNavigate();
	useEffect(()=>{
		navigate("/bbslist");
	})
	return (
		<div>
			<h2 style={{"color":"white"}}>Rive 게시판</h2>
		</div>
	);
}

export default Home;