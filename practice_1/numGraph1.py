#encoding utf-8
numDict={
0:"""  ****  \n *    * \n *    * \n *    * \n *    * \n *    * \n *    * 
  ****  """,
1:"""    *   \n  * *   \n *  *   \n*   *   \n    *   \n    *   
    *   \n  ***** """,
2:"""   ***   \n *     *\n *     *\n      * \n     *  \n   *    \n *      
 ****** """,
3:"""  ****  \n *    * \n      * \n   ***  \n      * \n       *\n *    * 
  ****  """,
4:""" *    * \n *    * \n *    * \n *    * \n ****** \n      * \n      * 
      * """,
5:""" ****** \n *      \n *      \n ****   \n     *  \n      * \n     *  
  ***   """,
6:"""  ***** \n *      \n *      \n *****  \n *    * \n *    * \n *    * 
  ****  """,
7:""" ****** \n      * \n     *  \n    *   \n    *   \n    *   \n    *   
    *   """,
8:"""  ****  \n *    * \n *    * \n  ****  \n *    * \n *    * \n *    * 
  ****  """,
9:"""  ****  \n *    * \n *    * \n *    * \n  ***** \n      * \n *    * 
  ****  """}
n=raw_input("Enter some figure: ")
try:
    num=int(n)
except:
    print("This isn't a figure")
else:
    if len(n)==1:
        print(numDict[num])
    else:
        print("enter only one figure")
