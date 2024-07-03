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
		fetch(`/api/users/chackId?username=${id}`)
		.then(res=>{return res.json()})
		.then(data=>{
			setCheckId(data.Check_sum);
			if(!data.Check_sum)
				alert("사용 가능한 아이디입니다.");
			else
				alert("이미 존재하는 아이디입니다.");
			console.log("check", data.Check_sum);
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

		const req = {
			id: id,
			name, name,
			pwd: pwd,
			checkPwd: checkPwd,
			email: email
		}
		console.log("join", checkId);
		if(checkId){
			alert("아이디 중복여부를 확인해 주세요.");
			return;
		}
		else if(checkPwd !== pwd){
			alert("비밀번호를 다시 확인해 주세요.")
			return;
		}

		fetch(`/api/users/create`, {
			method: "POST",
			headers: {
				'accept': 'application/json', 
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				username: id,
				user_pw: pwd,
				create_date: "123123"
			})
		})
		.then(res=>{
			alert(id + "님 회원가입을 축하드립니다 🎊");
			navigate("/bbslist");
		})
		.catch(err=>{
			alert(err.response.data);
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
							<button className="btn btn-outline-danger" onClick={checkIdDuplicate}><i className="fas fa-check"></i> 아이디 중복 확인</button>
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
				</tbody>
			</table><br />

			<div className="my-3 d-flex justify-content-center">
				<button className="btn btn-outline-secondary" onClick={join}><i className="fas fa-user-plus"></i> 회원가입</button>
			</div>

		</div>
	);
}

export default Join;