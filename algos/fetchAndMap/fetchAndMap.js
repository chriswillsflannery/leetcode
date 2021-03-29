// Given an end point URL to fetch all the posts and comments. Do the following.
// Map all the comments to the posts it belongs to. The resultant data after mapping should be of below structure.

//service.js
const POSTS_URL = `https://jsonplaceholder.typicode.com/posts`;
const COMMENTS_URL = `https://jsonplaceholder.typicode.com/comments`;

const fetchAllPosts = () => {
  return fetch(POSTS_URL).then(res => res.json());
};

const fetchAllComments = () => {
  return fetch(COMMENTS_URL).then(res => res.json());
};

const fetchData = async () => {
  const [posts, comments] = await Promise.all([
    fetchAllPosts(),
    fetchAllComments()
  ]);

  const grabAllCommentsForPost = postId =>
    comments.filter(comment => comment.postId === postId);

  const mappedPostWithComment = posts.reduce((acc, post) => {
    const allComments = grabAllCommentsForPost(post.id);
    acc[post.id] = allComments;
    return acc;
  }, {});

  console.log("mappedPostWithComment ", mappedPostWithComment);
};

fetchData();