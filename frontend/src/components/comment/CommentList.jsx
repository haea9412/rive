import { useState, useEffect } from "react";
// import Pagination from "react-js-pagination";
import Comment from "./Comment.jsx";

function CommentList(props) {

	const seq = Number(props.seq);

	// Paging
	const [page, setPage] = useState(0);
	const [totalCnt, setTotalCnt] = useState(0);

	const [commentList, setCommentList] = useState([]);

	const changePage = () => {
		setPage(page);
		getCommentList(page);
	}

	const getCommentList = async () => {
		fetch(`/api/answer/list?post_id=${seq}`,{
			method: "POST"
		})
		.then((res)=>{
			return res.json();
		})
		.then(data=>{
			console.log(data);
			// setCommentList(commentlists(data));
			setCommentList(data);
		})
		.catch((err) => {
			console.log("[BbsComment.js] getCommentList() error :<");
			console.log(err);
		});
	}

	useEffect(() => {
		getCommentList(1);
	}, []);

	return (
		<>
			<div className="my-1 d-flex justify-content-center">
				<h5><i className="fas fa-paperclip"></i> 댓글 목록 </h5>
			</div>

			{/* <Pagination
				activePage={page}
				itemsCountPerPage={5}
				totalItemsCount={totalCnt}
				pageRangeDisplayed={5}
				prevPageText={"‹"}
				nextPageText={"›"}
				onChange={changePage} /> */}
			{
				commentList.filter(obj=>obj.post_id === seq).map(function (comment, idx) {
					return (
						<div className="my-5" key={idx}>
							<Comment obj={comment} key={idx} />
						</div>
					);
				})
			}

		</>

	);
}


export default CommentList;