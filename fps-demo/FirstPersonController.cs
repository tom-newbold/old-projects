using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent(typeof(CharacterController))]
public class FirstPersonController : MonoBehaviour
{
    private bool m_IsWalking;
    [SerializeField] private float m_WalkSpeed = 1f;
    private bool m_IsCrouching;
    [SerializeField] private float m_CrouchSpeed = 1f;
    [SerializeField] private float m_RunSpeed = 1f;
    [SerializeField] private float m_JumpSpeed = 5f;
    [SerializeField] private float m_StickToGroundForce = 1f;
    [SerializeField] private float m_GravityMultiplier = 1f;
    [SerializeField] private float baseHeight = 2f;
    [SerializeField] private float crouchHeight = 1.4f;
    [SerializeField] private float crouchSpeed = 1f;
    [SerializeField] private float Xsensitivity = 2.5f;
    [SerializeField] private float Ysensitivity = 2.5f;
    public bool smooth = false;
    public float smoothTime = 5f;
    public bool lockCursor = true;
    public bool cursorIsLocked = true;

    public LayerMask ItemMask;
    public LayerMask EnvironMask;
    private Transform heldItem;
    private float heldDistance;
    private bool holding = false;
    public float reachDis = 10f;
    public float objSpeed = 8f;

    private Camera m_Camera;
    private Quaternion m_CharacterTargetRot;
    private Quaternion m_CameraTargetRot;
    private bool m_Jump;
    private Vector2 m_Input = new Vector2();
    private Vector3 m_MoveDir = Vector3.zero;
    private CharacterController m_CharacterController;
    public Vector3 spawnPoint = new Vector3(0, 2f, 0);
    private CollisionFlags m_CollisionFlags;
    private bool m_PreviouslyGrounded;
    private bool m_Jumping;
    void Start()
    {
        m_CharacterController = GetComponent<CharacterController>();
        m_Camera = Camera.main;
        m_Jumping = false;
        m_CharacterTargetRot = m_CharacterController.transform.localRotation;
        m_CameraTargetRot = m_Camera.transform.localRotation;
    }

    // Update is called once per frame
    void Update()
    {
        //get mouse input
        float yRot = Input.GetAxis("Mouse X") * Xsensitivity;
        float xRot = Input.GetAxis("Mouse Y") * Ysensitivity;

        //set and clamp rotations of character and camera
        m_CharacterTargetRot *= Quaternion.Euler(0f, yRot, 0f);
        m_CameraTargetRot *= Quaternion.Euler(-xRot, 0f, 0f);

        m_CameraTargetRot = ClampQuaternion(m_CameraTargetRot);

        Transform character = m_CharacterController.transform;
        Transform camera = m_Camera.transform;
        
        //apply rotations to objects
        if (smooth)
        {
            character.localRotation = Quaternion.Slerp(character.localRotation, m_CharacterTargetRot, smoothTime * Time.deltaTime);
            camera.localRotation = Quaternion.Slerp(camera.localRotation, m_CameraTargetRot, smoothTime * Time.deltaTime);
        }
        else
        {
            character.localRotation = m_CharacterTargetRot;
            camera.localRotation = m_CameraTargetRot;
        }

        //check and update cursor lock state
        UpdateCursorLock();

        //get jump input
        if (!m_Jump)
        {
            m_Jump = Input.GetButtonDown("Jump");
        }

        //no gravity if grounded
        if (!m_PreviouslyGrounded && m_CharacterController.isGrounded)
        {
            m_MoveDir.y = 0f;
            m_Jumping = false;
        }
        if (!m_CharacterController.isGrounded && !m_Jumping && m_PreviouslyGrounded)
        {
            m_MoveDir.y = 0f;
        }
        m_PreviouslyGrounded = m_CharacterController.isGrounded;

        if(m_CharacterController.transform.position.y <= -3)
        {
            m_CharacterController.transform.position = spawnPoint;
        }

        //holding obj input
        if (Input.GetMouseButton(0))
        {
            if (Input.GetMouseButtonDown(0))
            {
                //print("clicked");
                Ray ray = m_Camera.ScreenPointToRay(Input.mousePosition);
                RaycastHit lookingAtItem;
                if (Physics.Raycast(ray, out lookingAtItem, reachDis, ItemMask))
                {
                    heldItem = lookingAtItem.transform;
                    heldDistance = lookingAtItem.distance;
                    Rigidbody rb = heldItem.GetComponent<Rigidbody>();
                    rb.useGravity = false;
                    holding = true;
                }
            }
        } else
        {
            holding = false;
            if(heldItem != null)
            {
                Rigidbody rb = heldItem.GetComponent<Rigidbody>();
                rb.useGravity = true;
                heldItem = null;
            }
        }
        //print("holding = " + holding.ToString());
    }

    private void FixedUpdate()
    {
        float speed;
        GetInput(out speed);
        float distanceDelta = (baseHeight - crouchHeight) * Time.deltaTime * crouchSpeed;
        if (m_IsCrouching)
        {
            m_CharacterController.height = crouchHeight;
            m_CharacterController.center = new Vector3(0,(crouchHeight - baseHeight) / 2,0);
            m_Camera.transform.localPosition = Vector3.MoveTowards(m_Camera.transform.localPosition,new Vector3(0, crouchHeight - baseHeight/2, 0), distanceDelta);
        } else
        {
            m_CharacterController.height = baseHeight;
            m_CharacterController.center = new Vector3(0, 0, 0);
            m_Camera.transform.localPosition = Vector3.MoveTowards(m_Camera.transform.localPosition, new Vector3(0, baseHeight / 2, 0), distanceDelta);
        }
        //move in direction being aimed
        Vector3 desiredMove = transform.forward * m_Input.y + transform.right * m_Input.x;

        //get a normal for the surface that is being touched to move along it
        RaycastHit hitInfo;
        Physics.SphereCast(transform.position, m_CharacterController.radius, Vector3.down, out hitInfo,
                           m_CharacterController.height / 2f, Physics.AllLayers, QueryTriggerInteraction.Ignore);
        desiredMove = Vector3.ProjectOnPlane(desiredMove, hitInfo.normal);

        m_MoveDir.x = desiredMove.x * speed;
        m_MoveDir.z = desiredMove.z * speed;

        if (m_CharacterController.isGrounded)
        {
            //grounds player
            m_MoveDir.y = -m_StickToGroundForce;
            if (m_Jump)
            {
                m_MoveDir.y = m_JumpSpeed;
                m_Jump = false;
                m_Jumping = true;
            }
        }
        else
        {
            m_MoveDir += Physics.gravity * m_GravityMultiplier * Time.fixedDeltaTime;
        }
        m_CollisionFlags = m_CharacterController.Move(m_MoveDir * Time.fixedDeltaTime);

        //held object movement
        if (holding && heldItem != null)
        {
            Ray ray = m_Camera.ScreenPointToRay(Input.mousePosition);
            RaycastHit lookingAtItem;
            if (Physics.Raycast(ray, out lookingAtItem, reachDis, EnvironMask))
            {
                if(lookingAtItem.distance < heldDistance)
                {
                    heldDistance = lookingAtItem.distance;
                }
            }

            Vector3 target = ray.GetPoint(heldDistance);
            Vector3 dir = target - heldItem.position;
            Rigidbody rb = heldItem.GetComponent<Rigidbody>();

            //method 1: moves directly to position, however no momentum conserved
            //rb.MovePosition(heldItem.position + dir * Time.fixedDeltaTime * objSpeed);

            //method 2: forces applied, more natural movement, prone to sudden accelerations (orbiting/rubber-banding)
            //rb.AddForce(dir * Mathf.Log(dir.magnitude) * objSpeed);

            //method 3: best!!
            rb.velocity = dir * objSpeed / Mathf.Pow(rb.mass,0.5f);
        }

        UpdateCursorLock();
    }

    private Quaternion ClampQuaternion(Quaternion q)
    {
        q.x /= q.w;
        q.y /= q.w;
        q.z /= q.w;
        q.w = 1.0f;
        float angleX = 2.0f * Mathf.Rad2Deg * Mathf.Atan(q.x);
        angleX = Mathf.Clamp(angleX, -90f, 90f);
        q.x = Mathf.Tan(0.5f * Mathf.Deg2Rad * angleX);
        return q;
    }

    private void UpdateCursorLock()
    {
        if (lockCursor) {
            if (Input.GetKeyUp(KeyCode.Escape))
            {
                cursorIsLocked = false;
            }
            else if (Input.GetMouseButtonUp(0))
            {
                cursorIsLocked = true;
            }

            if (cursorIsLocked)
            {
                Cursor.lockState = CursorLockMode.Locked;
                Cursor.visible = false;
            }
            else if (!cursorIsLocked)
            {
                Cursor.lockState = CursorLockMode.None;
                Cursor.visible = true;
            }
        }
    }

    private void GetInput(out float speed)
    {
        //get input
        float horizontal = Input.GetAxis("Horizontal");
        float vertical = Input.GetAxis("Vertical");

        m_IsWalking = !Input.GetKey(KeyCode.LeftShift);
        m_IsCrouching = Input.GetKey(KeyCode.LeftControl);

        //set the desired speed to be walking or running
        speed = m_IsCrouching ? m_CrouchSpeed: (m_IsWalking ? m_WalkSpeed : m_RunSpeed);
        m_Input = new Vector2(horizontal, vertical);
        if(m_Input.magnitude > 1)
        {
            m_Input.Normalize();
        }
    }

    private void OnControllerColliderHit(ControllerColliderHit hit)
    {
        //handle collisions with other rigidbodies
        Rigidbody body = hit.collider.attachedRigidbody;
        //dont move the rigidbody if the character is on top of it
        if (m_CollisionFlags == CollisionFlags.Below)
        {
            return;
        }
        if (body == null || body.isKinematic)
        {
            return;
        }
        body.AddForceAtPosition(m_CharacterController.velocity * 0.1f, hit.point, ForceMode.Impulse);
    }
}
