/* 로그인 컴포넌트 */
import { useState, useContext } from "react";
import { useNavigate } from "react-router";
import { AuthContext } from "../context/AuthProvider";
import { HttpHeadersContext } from "../context/HttpHeadersProvider";

function Login() {

	const { auth, setAuth } = useContext(AuthContext);
	const { headers, setHeaders } = useContext(HttpHeadersContext);

	const navigate = useNavigate();

	const [id, setId] = useState("");
	const [pwd, setPwd] = useState("");

	const changeId = (event) => {
		setId(event.target.value);
	}

	const changePwd = (event) => {
		setPwd(event.target.value);
	}

	const login = async () => {
		const req = {
			id: id,
			pwd: pwd
		}

		fetch(`/api/users/login/token`,{
			method: "POST",
			headers: {
				'accept': ' application/json',
				'Content-Type': ' application/x-www-form-urlencoded',
			},
			body: `grant_type=&username=${id}&password=${pwd}&scope=&client_id=&client_secret=`
		})
		.then(res=>{
			console.log(res);
			if(res.status === 200){
				return res.json();
			}
			return false;
		})
		.then(data=>{
			if(data){
				// JWT 토큰 저장
				localStorage.setItem("bbs_access_token", data.token_type);
				localStorage.setItem("id", data.username);
				setAuth(data.username);
				setHeaders({"Authorization": `${data.token_type} ${data.access_token}`}); // 헤더 Authorization 필드 저장
				navigate("/bbslist");
			}
			else{
				alert("아이디 또는 비밀번호가 틀립니다.");
			}
		})
		.catch((err) => {
			console.log("[Login.js] login() error :<");
			console.log(err);

			alert("⚠️ " + err.response.data);
		});
	}

	return (
		<div>
			<table className="table">
				<tbody>
					<tr>
						<th className="col-3">아이디</th>
						<td>
							<input type="text" value={id} onChange={changeId} size="50px" />
						</td>
					</tr>

					<tr>
						<th>비밀번호</th>
						<td>
							<input type="password" value={pwd} onChange={changePwd} size="50px" />
						</td>
					</tr>
				</tbody>
			</table><br />

			<div className="my-1 d-flex justify-content-center">
				<button className="btn btn-outline-secondary" onClick={login}><i className="fas fa-sign-in-alt"></i> 로그인</button>
			</div>

		</div>
	);
}

export default Login;