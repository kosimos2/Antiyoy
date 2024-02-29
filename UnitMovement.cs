using UnityEngine;

public class UnitMovement : MonoBehaviour
{
    public static int Score_Hex;
    // Start is called before the first frame update
    void Start()
    {
        Score_Hex = 0;
    }
    // Update is called once per frame
    void Update()
    {
        
        if (Input.GetMouseButtonDown(0)) // ���������, ���� �� ������ ����� ������ ����
        {
            Vector2 mousePosition = Camera.main.ScreenToWorldPoint(Input.mousePosition); // �������� ������� ���� � ������� �����������

            RaycastHit2D hit = Physics2D.Raycast(mousePosition, Vector2.zero); // ������� ��� �� ������� ����

            if (hit.collider != null) // ���������, ����� �� ��� �� ���������
            {
                Hex hex = hit.collider.GetComponent<Hex>();
                Debug.Log(message: "UnitMovement == "+ hex.Unit + " + " + Score_Hex);

                if (hex.Unit == null && Score_Hex == 0)
                {
                    Score_Hex = 0;
                }
                else if (hex.Unit != null && Score_Hex == 0)
                {
                    Score_Hex = 1;                  
                }
                else if (hex.Unit == null && Score_Hex == 1)
                {
                    Score_Hex = 2;
                }
                else if (hex.Unit != null && Score_Hex == 2)
                {
                    Score_Hex = 0;
                }
            }
        }

    }
    


}
