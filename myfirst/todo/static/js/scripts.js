/* Если javascript работает, скроет предупреждающую надпись*/
$(function() {
	$("#test_working_js").addClass("d-none");
});


function get_csrf_token(){
	return $("input[name=csrfmiddlewaretoken]").val()
}

/* Если javascript работает, скроет кнопки предназначение для работы по GET запросам
   и сделает видимыми кнопки, отправляющие ajax запросы */
function display_available_control_buttons() {
	$(".js_buttons").each(function(){
		$(this).toggleClass("d-none");
		$(this).toggleClass("d-flex");
	});

	$(".url_buttons").each(function(){
		$(this).remove();
	});
}


function display_available_filter_buttons() {
	$(".js_filter_buttons").each(function(){
		$(this).toggleClass("d-none");
	});

	$(".url_filter_buttons").each(function(){
		$(this).remove();
	});
}


/* Изменение состояния задания (выполнено /не выполнено)*/
function change_task_status(data){
	if(data.responseJSON.result === "ok"){
		if(data.responseJSON.is_completed === false){
			$("#mark"+data.responseJSON.task_id).toggleClass("d-none");
			$("#complete-control-button"+data.responseJSON.task_id).toggleClass("d-none");
			$("#uncomplete-control-button"+data.responseJSON.task_id).removeClass("d-none");
			$("#accordion-item-"+data.responseJSON.task_id).removeClass("task-state-completed");
			$("#accordion-item-"+data.responseJSON.task_id).addClass("task-state-uncompleted");
		}
		if(data.responseJSON.is_completed === true){
			$("#mark"+data.responseJSON.task_id).toggleClass("d-none");
			$("#complete-control-button"+data.responseJSON.task_id).toggleClass("d-none");
			$("#uncomplete-control-button"+data.responseJSON.task_id).toggleClass("d-none");
			$("#accordion-item-"+data.responseJSON.task_id).removeClass("task-state-uncompleted");
			$("#accordion-item-"+data.responseJSON.task_id).addClass("task-state-completed");
		}
	}
}


function show_completed_tasks(){
	$(".task-state-completed").each(function(){
		$(this).removeClass("d-none");
	});

	$("#js_filter_button_completed").addClass("btn-outline-primary-hover")
	$("#js_filter_button_uncompleted").removeClass("btn-outline-primary-hover")
	$("#js_filter_button_all").removeClass("btn-outline-primary-hover")
}


function hide_completed_tasks(){
	$(".task-state-completed").each(function(){
		$(this).addClass("d-none");
	});
}


function show_uncompleted_tasks(){
	$(".task-state-uncompleted").each(function(){
		$(this).removeClass("d-none");
	});

	$("#js_filter_button_uncompleted").addClass("btn-outline-primary-hover")
	$("#js_filter_button_completed").removeClass("btn-outline-primary-hover")
	$("#js_filter_button_all").removeClass("btn-outline-primary-hover")
}


function hide_uncompleted_tasks(){
	$(".task-state-uncompleted").each(function(){
		$(this).addClass("d-none");
	});
}


function all_tasks(){
	show_completed_tasks();
	show_uncompleted_tasks();

	$("#js_filter_button_all").addClass("btn-outline-primary-hover")
	$("#js_filter_button_uncompleted").removeClass("btn-outline-primary-hover")
	$("#js_filter_button_completed").removeClass("btn-outline-primary-hover")
}


function completed_tasks(){
	show_completed_tasks();
	hide_uncompleted_tasks();
}


function uncompleted_tasks(){
	show_uncompleted_tasks();
	hide_completed_tasks();
}


function append_task_handler(data){
	if(data.responseJSON.result === "ok"){

        div = $("<div id='accordion-item-" + data.responseJSON.task_id + "' class='accordion-item task-state-uncompleted'>"+
         			"<h2 class='accordion-header' id='headingOne'>"+
            			"<button class='accordion-button collapsed' type='button' data-bs-toggle='collapse' "+ 
              				"data-bs-target='#collapse" + data.responseJSON.task_id + "' aria-expanded='false' "+ 
            				"aria-controls='collapse" + data.responseJSON.task_id + "'>"+
            				"<div class='d-none' id='mark" + data.responseJSON.task_id + "'>"+
               					"<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-check2-square' viewBox='0 0 16 16'>"+
                  				"<path d='M3 14.5A1.5 1.5 0 0 1 1.5 13V3A1.5 1.5 0 0 1 3 1.5h8a.5.5 0 0 1 0 1H3a.5.5 0 0 0-.5.5v10a.5.5 0 0 0 .5.5h10a.5.5 0 0 0 .5-.5V8a.5.5 0 0 1 1 0v5a1.5 1.5 0 0 1-1.5 1.5H3z'/>"+
                  				"<path d='M8.354 10.354l7-7a.5.5 0 0 0-.708-.708L8 9.293 5.354 6.646a.5.5 0 1  0-.708.708l3 3a.5.5 0 0 0 .708 0z'/>"+
                				"</svg>"+
             				"</div>"+      
              				"<span class='px-2'>" + data.responseJSON.task_title + "</span>"+
            			"</button>"+
          			"</h2>"+
          		"<div id='collapse" + data.responseJSON.task_id + "' class='accordion-collapse collapse' aria-labelledby='headingOne' data-bs-parent='#accordionExample'>"+
            		"<div class='accordion-body'>" + data.responseJSON.task_title + "</div>"+
            		"<div id='comment-container-" + data.responseJSON.task_id + "'></div>"+
            		"<div class='container accordion-body js_buttons d-flex'>"+
						
		              	"<div id='complete-control-button" + data.responseJSON.task_id + "' class='d-none'>"+
		                "<button type='button' class='me-1 btn btn-outline-warning' "+
		                "onclick=make_change_task_status_requests('/todo/api_set_uncompleted_status'," + data.responseJSON.task_id + ")>Снять отметку</button>"+   
		             	"</div>"+
            			
		              	"<div id='uncomplete-control-button" + data.responseJSON.task_id + "' class='d-flex'>"+
		                "<button type='button' class='me-1 btn btn-outline-primary' "+
		                "onclick=make_change_task_status_requests('/todo/api_set_completed_status'," + data.responseJSON.task_id + ")>Отметить как выполненая</button>"+   
		             	"</div>"+

		             	"<button type='button' class='btn btn-outline-secondary me-1' data-bs-toggle='modal' data-bs-target='#addComment'"+
		             	"onclick=add_task_id_to_modal_form(" + data.responseJSON.task_id + ")> Добавить комментарий </button>"+
		             	"<button type='button' class='me-1 btn btn-outline-danger' "+
		             	"onclick=make_delete_task_requests('/todo/api_delete_task'," + data.responseJSON.task_id + ")>Удалить задачу</button>"+
        			"</div>")
        $("#task-conteiner").prepend(div)
		}
}



function delete_task_handler(data){
	if(data.responseJSON.result === "ok"){
			$("#accordion-item-"+data.responseJSON.task_id).remove();
		}

	/* Если удалили все елементы */
	if($(".accordion-item").length === 1){
		$("#empty-tasks-alert").toggleClass("d-none");
	}
}


function append_comment_handler(data){
	if(data.responseJSON.result === "ok"){

		div = $("<div id='comment-body-" + data.responseJSON.comment_id + "' class='accordion-body my-0 py-1'>"+
                  "<div class='alert alert-secondary py-1 my-0' role='alert'>"+
                    "<div class='row g-3'>"+
                      "<!-- Кнопки для отправки ajax запросов -->"+
                      "<a type='button' class='col-auto btn-close js_buttons d-flex'"+
                        "onclick=make_delete_comment_requests('api_delete_comment'," + data.responseJSON.comment_id + ")></a>"+
                    "<div class='col-auto'><span>" + data.responseJSON.comment_text + "</span></div>" +
                  "<div class='col-auto'></div>" +
                "</div>")

        $("#comment-container-"+data.responseJSON.task_id).prepend(div)
		}
}


function delete_comment_handler(data){
	if(data.responseJSON.result === "ok"){
			$("#comment-body-"+data.responseJSON.comment_id).remove();
		}
}


function make_append_task_requests(url_, post_data) {
	$.ajax({url: url_, type: "POST", data: post_data, complete: append_task_handler});
}


function make_delete_task_requests(url_, task_id) {
	let post_data = {
		"task_id": task_id,
		"csrfmiddlewaretoken": get_csrf_token(),
	}

	$.ajax({url: url_, type: "POST", data: post_data, complete: delete_task_handler});
}


function make_append_comment_requests(url_, post_data) {
	$.ajax({url: url_, type: "POST", data: post_data, complete: append_comment_handler});
}


function make_delete_comment_requests(url_, comment_id) {
	let post_data = {
		"comment_id": comment_id,
		"csrfmiddlewaretoken": get_csrf_token(),
	}

	$.ajax({url: url_, type: "POST", data: post_data, complete: delete_comment_handler});
}


function make_change_task_status_requests(url_, task_id) {
	var post_data = {
		"task_id": task_id, 
		"csrfmiddlewaretoken": get_csrf_token(),
	}

	$.ajax({url: url_, type: "POST", data: post_data, complete: change_task_status});
}


/* */
function add_task_id_to_modal_form(task_id){
	$("input#comment-task-id").attr("value", task_id)
}


function api_append_comment(url){
	let data = {
		"text": $("textarea#comment-body").val(),
		"task_id": $("input#comment-task-id").val(),
		"csrfmiddlewaretoken": get_csrf_token(),
	}

	/* Стирает введенный текст с формы добавления комментария */
	$("textarea#comment-body").val("")

	make_append_comment_requests(url, data);

}

function api_append_task(url){
	let data = {
		"title": $("#task-title-input").val(),
		"text": $("#task-text-input").val(),
		"csrfmiddlewaretoken": get_csrf_token(),
	}

	/* Стирает введенный текст с формы добавления задачи */
	$("#task-title-input").val(""),
	$("#task-text-input").val(""),

	make_append_task_requests(url, data);

}


function main (jQuery){
	/* Если js работает, скроет кнопки, отправляющие GET запросы 
	и сделает видимыми кнопки, использующие ajax запросы.
	Нужно для увеличения отклика сайта на действия пользователя. SPA*/
	display_available_control_buttons();
	/* 
	Аналогично для кнопок "фильтров".  
	Если url кнопки заменить на привязанные к javascript функциям, при смене типов заданий 
	(выполненных, невыполненных) сервер не будет присылать новую html страницу а, 
	javascript функции (all_tasks, completed_tasks, uncompleted_tasks) 
	будут скрывать ненужные и отображать нужные элементы.
	*/
	display_available_filter_buttons();
}

/* Ждет полной загрузки страницы и запускает функцию main */
$(document).ready(main);