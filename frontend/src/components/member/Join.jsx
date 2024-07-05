/* 회원가입 컴포넌트 */
import { useState } from "react";
import { useNavigate } from "react-router";

function Join() {

	const [id, setId] = useState("");
	const [name, setName] = useState("");
	const [pwd, setPwd] = useState("");
	const [checkPwd, setCheckPwd] = useState("");
	const [email, setEmail] = useState("");
	const [checkId, setCheckId] = useState(true);

	const navigate = useNavigate();

	const changeId = (event) => {
		setCheckId(true);
		setId(event.target.value);
		console.log("change Id");
	}

	const changeName = (event) => {
		setName(event.target.value);
	}

	const changePwd = (event) => {
		setPwd(event.target.value);
	}

	const changeCheckPwd = (event) => {
		setCheckPwd(event.target.value);
	}

	const changeEmail = (event) => {
		setEmail(event.target.value);
	}

	/* 아이디 중복 체크 */
	const checkIdDuplicate = async () => {
		fetch(`/api/users/login`,{
			method: "POST",
			headers: {
				'accept': 'application/json',
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				username: id,
				user_pw: "passwd",
				create_date: "1900-01-01T00:00:00.000Z",

			})
		})
		.then(res=>{return res.json()})
		.then(data=>{
			setCheckId(data.Check_sum);
			if(!data.Check_sum)
				alert("사용 가능한 아이디입니다.");
			else
				alert("이미 존재하는 아이디입니다.");
			console.log("check", data);
		})
		.catch((err) => {
			console.log("[Join.js] checkIdDuplicate() error :<");
			console.log(err);

			const resp = err.response;
			if (resp.status == 400) {
				alert(resp.data);
			}
		});

	}

	/* 회원가입 */
	const join = async () => {
		fetch("/api/users/create",{
			method: "POST",
			headers: {
				'accept': ' */*',
				'Content-Type': ' application/json',
			},
			body: JSON.stringify({
				"username": id,
				"user_pw1": pwd,
				"user_pw2": checkPwd,
				"email": email,
			})
		})
		.then(res=>{
			console.log(res);
			switch (res.status) {
				case 204:
					alert(id + "님 회원가입을 축하드립니다 🎊");
					navigate("/bbslist");
					break;
				case 409:
					alert("이미 가입한 이메일입니다.");
					break;
				case 422:
					alert("모든 정보를 다시 확인해 주세요");
					break;
				default:
					console.log("???");
					break;
			}
		})
		.catch(err=>{
			alert(err.response);
		})
	}

	return (
		<div>
			<table className="table">
				<tbody>
					<tr>
						<th className="col-2">아이디</th>
						<td>
							<input type="text" value={id} onChange={changeId} size="50px" /> &nbsp; &nbsp;
							{/* <button className="btn btn-outline-danger" onClick={checkIdDuplicate}><i className="fas fa-check"></i> 아이디 중복 확인</button> */}
						</td>
					</tr>

					<tr>
						<th>비밀번호</th>
						<td>
							<input type="password" value={pwd} onChange={changePwd} size="50px" />
						</td>
					</tr>

					<tr>
						<th>비밀번호 확인</th>
						<td>
							<input type="password" value={checkPwd} onChange={changeCheckPwd} size="50px" />
						</td>
					</tr>

					<tr>
						<th>이메일</th>
						<td>
							<input type="email" value={email} pattern=".+@example\.com" onChange={changeEmail} size="100px" />
						</td>
					</tr>
				</tbody>
			</table><br />

			<div className="my-3 d-flex justify-content-center">
				<button className="btn btn-outline-secondary" onClick={join}><i className="fas fa-user-plus"></i> 회원가입</button>
			</div>

		</div>
	);
}

export default Join;