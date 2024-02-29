using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Unit : MonoBehaviour
{
    public string Team;
    public string Type;
    public GameObject standingUnit;
    public GameObject hexagonObject;

    private bool isDragging = false;
    private Vector3 offset;


    // Start is called before the first frame update
    void Start()
    {
        
    }

    void OnMouseDown()
    {
        

        if (isDragging == false)
        {
            Debug.Log("if (isDragging == false)");
            offset = transform.position - Camera.main.ScreenToWorldPoint(Input.mousePosition);
            isDragging = true;
            Debug.Log("--------------");
        }
        else if (isDragging == true)
        {
            Debug.Log("if (isDragging == true)");
            Vector3 newPosition = Camera.main.ScreenToWorldPoint(Input.mousePosition) + offset;
            transform.position = new Vector3(newPosition.x, newPosition.y, 0);
            isDragging = false;
            Debug.Log("++++++++++++++++");

        }
        
        
    
        
        // Остановить анимацию движения
       



    }




    // Update is called once per frame
    void Update()
    {
        
    }
}
