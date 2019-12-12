/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function(root) {
    function help(n1, n2) {
        if (n1 === null && n2 === null) {
            return true;
        }
        if (n1 === null || n2 === null) {
            return false;
        }
        return n1.val === n2.val && help(n1.left, n2.right) && help(n1.right, n2.left);
    }
    
    return root === null? true: help(root.left, root.right);
};