import { useContext, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { AuthContext } from "../context/AuthProvider";
import { HttpHeadersContext } from "../context/HttpHeadersProvider";

function BbsWrite() {

	const { auth, setAuth } = useContext(AuthContext)
	const { headers, setHeaders } = useContext(HttpHeadersContext);

	const navigate = useNavigate();

	const [title, setTitle] = useState("");
	const [content, setContent] = useState("");

	const changeTitle = (event) => {
		setTitle(event.target.value);
	}

	const changeContent = (event) => {
		setContent(event.target.value);
	}

	/* [POST /bbs]: 게시글 작성 */
	const createBbs = async() => {

		const req = {
			id: localStorage.getItem("id"), 
			title: title, 
			content: content
		}

		fetch("/api/posts/create",{
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"accept": "*/*"
			},
			body: JSON.stringify({
				"type": 1,
				"user_id": 1,
				"title": title,
				"content": content,
				"create_date": new Date(),
			})
		})
		.then((res)=>{
			navigate(`/bbslist`); // 새롭게 등록한 글 상세로 이동
		})
	}

	useEffect(() => {
		if (!auth) {
			alert("로그인 한 사용자만 게시글을 작성할 수 있습니다 !");
			navigate(-1);
		}
	}, []);


	return (
		<div>
			<table className="table">
				<tbody>
					{/* <tr>
						<th className="table-dark text-center">작성자</th>
						<td>
							<input type="text" className="form-control"  value={localStorage.getItem("id")} size="50px" readOnly />
						</td>
					</tr> */}

					<tr>
						<th className="table-dark text-center">제목</th>
						<td>
							<input type="text" className="form-control" value={title} onChange={changeTitle} size="50px" />
						</td>
					</tr>

					<tr>
						<th className="table-dark text-center">내용</th>
						<td>
							<textarea className="form-control" value={content} onChange={changeContent} rows="10"></textarea>
						</td>
					</tr>
				</tbody>
			</table>

			<div className="my-5 d-flex justify-content-center">
				<button className="btn btn-outline-secondary" onClick={createBbs}><i className="fas fa-pen"></i> 등록하기</button>
			</div>
		</div>
	);
}

export default BbsWrite;